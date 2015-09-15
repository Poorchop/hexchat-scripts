#!/usr/bin/env python3

import requests
import sys
import threading
import hexchat

__module_name__ = "Twitch Title"
__module_author__ = "Poorchop"
__module_version__ = "0.2"
__module_description__ = "Display stream status and description for TwitchTV streams"
# TODO: Clean up thread handling <Poorchop>
# TODO: Figure out why get_current_status() sometimes doesn't print updated status <Poorchop>

t = None


class StreamParser:

    def __init__(self, channel):
        self.url = "https://api.twitch.tv/kraken/streams?"
        self.channel = channel
        self.twitch_chans = []
        self.status = ""
        self.display_name = ""
        self.game = ""
        self.title = ""

    def set_topic(self):
        """
        Set the channel topic (no formatting) and print the topic locally with formatting
        """
        msg = "\00318{0}\00399 - {1} | Now playing: \00318{2}\00399 | {3}"\
            .format(self.display_name, self.status, self.game, self.title)
        hexchat.prnt(msg)
        # HexChat doesn't support hiding characters in the topic bar (Windows), so strip the formatting until it's fixed
        if sys.platform == "win32":
            msg = hexchat.strip(msg, -1, 3)
        if hexchat.get_info("topic") != msg:
            hexchat.command("RECV :{0}!Topic@twitch.tv TOPIC #{0} :{1}".format(self.channel, msg))

    def get_twitch_channels(self):
        """
        Get a list of open TwitchTV channels and store them in self.twitch_chans
        """
        self.twitch_chans = []
        for chan in hexchat.get_list("channels"):
            if chan.type == 2 and chan.context.get_info("server") == "tmi.twitch.tv":
                self.twitch_chans.append(chan.channel)

    def update_status(self):
        """
        Check the status of open channels
        """
        if self.twitch_chans:
            for chan in self.twitch_chans:
                self.channel = chan[1:]
                self.get_stream_info()
                self.set_topic()
        else:
            pass

    def get_stream_info(self):
        """
        Get the stream information
        """
        params = {"channel": self.channel}
        r = requests.get(self.url, params=params)
        data = r.json()
        self.display_name = self.channel
        self.game = ""
        self.title = "\035Stream is offline\017"
        if not data["streams"]:
            self.status = "\00320\002OFFLINE\002\00399"
        else:
            self.status = "\00319\002LIVE\002\00399"
            self.display_name = data["streams"][0]["channel"]["display_name"]
            self.game = data["streams"][0]["channel"]["game"]
            self.title = data["streams"][0]["channel"]["status"]


def is_twitch():
    server = hexchat.get_info("server")
    if server and "twitch.tv" in server:
        return True
    else:
        return False


def get_current_status():
    """
    Update the stream status every 10 minutes
    """
    global t
    parser = StreamParser(channel=None)
    parser.get_twitch_channels()
    parser.update_status()
    t = threading.Timer(600, get_current_status)
    t.daemon = True
    t.start()


def join_cb(word, word_eol, userdata):
    """
    Set the topic immediately after joining a channel
    """
    if is_twitch():
        channel = hexchat.get_info("channel")[1:]
        parser = StreamParser(channel=channel)
        parser.get_stream_info()
        parser.set_topic()

    return hexchat.EAT_NONE


def unload_cb(userdata):
    """
    These appear to be necessary to prevent HexChat from crashing
    on quit while a thread is active in Python
    """
    global t
    t.cancel()
    t.join()


get_current_status()
hexchat.hook_print("Open Context", join_cb)
hexchat.hook_unload(unload_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

from datetime import datetime
import hexchat
import os
import re

__module_name__ = "URL Logger"
__module_author__ = "Poorchop"
__module_version__ = "0.1"
__module_description__ = "Log URLs from specific channels and PMs to disk"

#                    channels      PMs
watched_channels = ("#hexchat", "TingPing")

events = ("Channel Message", "Channel Action",
          "Channel Msg Hilight", "Channel Action Hilight",
          "Private Message", "Private Message to Dialog",
          "Private Action", "Private Action to Dialog")
# regex source: http://blog.mattheworiordan.com/post/13174566389/url-regular-expression-for-links-with-or-without-the
url_regex = re.compile("((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A"
                       "-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)")


def url_logger(stripped_word, nick, network, chan, time):
    directory = os.path.join(hexchat.get_info("configdir"), "logs", network, chan)
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = os.path.join(hexchat.get_info("configdir"), "logs", network, chan, "urls.txt")
    f = open(directory, "a")
    f.write(time + " " + nick + "@" + chan + ":" + network + " - " + stripped_word + "\n")
    f.close()


def url_finder(word, nick, network, chan, time):
    for w in word[1].split():
        stripped_word = hexchat.strip(w, -1, 3)
        if url_regex.match(stripped_word):
            url_logger(stripped_word, nick, network, chan, time)


def chan_check_cb(word, word_eol, userdata):
    word = [(word[i] if len(word) > i else "") for i in range(4)]
    chan = hexchat.get_info("channel")
    if chan in watched_channels:
        nick = hexchat.strip(word[0], -1, 3)
        time = datetime.now().strftime("[%b %d %Y %H:%M]")
        network = hexchat.get_info("network")
        url_finder(word, nick, network, chan, time)


for event in events:
    hexchat.hook_print(event, chan_check_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

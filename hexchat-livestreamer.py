import hexchat

__module_name__ = "HexChat Livestreamer"
__module_author__ = "PDog"
__module_version__ = "0.1"
__module_description__ = "Launch a Twitch.TV stream via Livestreamer when the corresponding channel is joined in HexChat"

def is_twitch():
    server = hexchat.get_info("server")
    if "twitch.tv" in server:
        return True
    else:
        return False

def join_channel_cb(word, word_eol, userdata):
    if is_twitch() and word[1][0] == "#":
        streamer = word[1][1:]
        hexchat.command("EXEC livestreamer twitch.tv/{0} best".format(streamer))

    return hexchat.EAT_NONE

def livestreamer_cb(word, word_eol, userdata):
    word = [(word[i] if len(word) > i else "") for i in range(3)]
    hexchat.command("EXEC livestreamer twitch.tv/{1} {2}".format(*word))

    return hexchat.EAT_ALL

hexchat.hook_command("JOIN", join_channel_cb)
hexchat.hook_command("LIVESTREAMER", livestreamer_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

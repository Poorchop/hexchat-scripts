import hexchat

__module_name__ = "Shorten Nicknames"
__module_author__ = "PDog"
__module_version__ = "0.0.2"
__module_description__ = "Truncate nicknames beyond a certain length"

# Set cutoff equal to the maximum character length you want in the nickname column
cutoff = 14

# Endless recursion prevention, copied this trick from:
# https://github.com/TingPing/plugins/blob/master/HexChat/wordhl.lua#L26
# TingTing is also the author of the offical hexchat documentation
# https://media.readthedocs.org/pdf/hexchat/2.9.5/hexchat.pdf
edited = False

def truncate_cb(word, word_eol, userdata):
    global edited
    if edited:
        return
    nickname = word[0]

    if len(nickname) > cutoff:
        edited = True
        new_nick = nickname[0:cutoff] + "~"
        hexchat.emit_print(userdata, new_nick, word[1])
        edited = False
        return hexchat.EAT_ALL

hexchat.hook_print("Channel Message", truncate_cb, "Channel Message")
hexchat.hook_print("Channel Msg Hilight", truncate_cb, "Channel Msg Hilight")
hexchat.prnt("Nick Shortener Version " + __module_version__ + " loaded!")

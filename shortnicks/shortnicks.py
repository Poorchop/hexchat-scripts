import hexchat

__module_name__ = "Shorten Nicknames"
__module_author__ = "PDog"
__module_version__ = "0.0.1"
__module_description__ = "Truncate nicknames beyond a certain length"

# Set cutoff equal to the maximum character length you want in the nickname column
cutoff = 14

def truncate_cb(word, word_eol, userdata):
    nickname = word[0]

    if len(nickname) > cutoff:
        new_nick = nickname[0:cutoff - 1] + "~"
        hexchat.emit_print(userdata, new_nick, word[1])
        return hexchat.EAT_ALL

hexchat.hook_print("Channel Message", truncate_cb, "Channel Message")
hexchat.hook_print("Channel Msg Hilight", truncate_cb, "Channel Msg Hilight")

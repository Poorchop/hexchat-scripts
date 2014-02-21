import hexchat

__module_name__ = "Nick Spy"
__module_author__ = "PDog"
__module_version__ = "0.1"
__module_description__ = "Colorize a channel name when certain users speak there"

nicknames = ["CleverNickname"]

def nickspy_cb(word, word_eol, userdata):
    if word[0] in nicknames or word[0].lower() in nicknames:
        context = hexchat.get_context()
        context.command("gui color 3")

        return hexchat.EAT_NONE

hexchat.hook_print("Channel Action", nickspy_cb)
hexchat.hook_print("Channel Message", nickspy_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

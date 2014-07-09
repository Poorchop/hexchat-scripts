import hexchat

__module_name__ = "Detach"
__module_author__ = "Poorchop"
__module_version__ = "0.1"
__module_description__ = "Detach and close the current channel on ZNC with a simple /detach"


def detach_cb(word, word_eol, userdata):
    if len(word) > 1:
        return
    else:
        chan = hexchat.get_info("channel")
        hexchat.command("QUOTE DETACH {}".format(chan))

    return hexchat.EAT_ALL


hexchat.hook_command("DETACH", detach_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

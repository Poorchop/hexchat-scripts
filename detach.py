import hexchat

__module_name__ = "Detach"
__module_author__ = "Poorchop"
__module_version__ = "0.1"
__module_description__ = "Detach and close the current channel on ZNC with a simple /detach"

detached = False


def detach_cb(word, word_eol, userdata):
    global detached

    if detached or len(word) > 1:
        return
    else:
        chan = hexchat.get_info("channel")
        detached = True
        hexchat.command("DETACH {}".format(chan))
        detached = False

    return hexchat.EAT_ALL


hexchat.hook_command("DETACH", detach_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

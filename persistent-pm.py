import hexchat

__module_name__ = "Persistent PM Tabs"
__module_author__ = "Poorchop"
__module_version__ = "0.1"
__module_description__ = "Restore previously open private message tabs after launching HexChat"


def closedialog_cb(word, word_eol, userdata):
    #TODO: check for existing dialogs to same user on other networks
    if hexchat.get_info("channel")[0] != "#":
        nick = hexchat.get_info("channel")
        hexchat.del_pluginpref("persistpm_" + nick)


def incomingdialog_cb(word, word_eol, userdata):
    nick = word[0]
    network = hexchat.get_info("network")
    hexchat.set_pluginpref("persistpm_" + nick, network)


def query_cb(word, word_eol, userdata):
    if len(word) > 1:
        nick = word[1]
        network = hexchat.get_info("network")
        hexchat.set_pluginpref("persistpm_" + nick, network)


def loadpm_cb(word, word_eol, userdata):
    #TODO: save dialogs to a single user across multiple networks
    for pref in hexchat.list_pluginpref():
        if pref[:10] == "persistpm_":
            saved_network = hexchat.get_pluginpref(pref)
            if saved_network == hexchat.get_info("network"):
                saved_nick = pref[10:]
                network_context = hexchat.find_context(channel=saved_network)
                network_context.command("QUERY {}".format(saved_nick))


hexchat.hook_print("Close Context", closedialog_cb)
hexchat.hook_print("Private Action to Dialog", incomingdialog_cb)
hexchat.hook_print("Private Message to Dialog", incomingdialog_cb)
hexchat.hook_command("QUERY", query_cb)
hexchat.hook_print("Motd", loadpm_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

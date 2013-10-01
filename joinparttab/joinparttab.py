import hexchat

__module_name__ = "Join/Part Tab"
__module_author__ = "PoorDog"
__module_version__ = "0.1"
__module_description__ = "Place join/part messages in a separate tab for designated servers"

hexchat.prnt (__module_name__ + " version " + __module_version__ + " loaded.")

# add your servers here
host_list = ["irc.twitch.tv", ]

# customize tab name to your liking
tab_name = "(Joins/Parts)"

def server_check():
    if hexchat.get_info("host") in host_list:
        return True
    else:
        return False

def jpfilter_cb(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    jp_context = hexchat.find_context(channel=tab_name)

    if server_check():
        if userdata == "Join":
            jp_context.prnt("{0} \00323*\t{1} has joined".format(channel, word[2]))
            return hexchat.EAT_ALL

        elif userdata == "Part":
            jp_context.prnt("{0} \00324*\t{1} has left".format(channel, word[1]))
            return hexchat.EAT_ALL
    else:
        # print join/part messages normally for all other servers
        return hexchat.EAT_NONE

hexchat.hook_print("Join", jpfilter_cb, "Join")
hexchat.hook_print("Part", jpfilter_cb, "Part")

hexchat.command("query {0}".format(tab_name))

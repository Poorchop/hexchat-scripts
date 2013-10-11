import hexchat

__module_name__ = "Join/Part Tab"
__module_author__ = "PoorDog"
__module_version__ = "1.2"
__module_description__ = "Place join/part/quit messages in a separate tab for designated servers and/or channels"

hexchat.prnt (__module_name__ + " version " + __module_version__ + " loaded.")

# customize tab name to your liking
tab_name = "(Joins/Parts)"

def get_network(name):
    return hexchat.get_pluginpref("jptab_" + name)

def jptab_pref(word, word_eol, userdata):
    network = hexchat.get_info("network")
    channel = hexchat.get_info("channel")

    if len(word) == 3:
    
        if word[2].lower() == "network" and network != tab_name:
            if word[1].lower() == "add":
                hexchat.set_pluginpref("jptab_" + network, "network")
                hexchat.prnt("*\tNetwork \00319{}\00399 added to joint/part filters".format(network))
                load_jpfilters()
            elif word[1].lower() == "remove":
                hexchat.del_pluginpref("jptab_" + network)
                hexchat.prnt("*\tNetwork \00319{}\00399 removed from joint/part filters".format(network))
                load_jpfilters()
            else:
                hexchat.prnt("Usage: /jptab [add|remove] network")

        elif word[2].lower() == "channel" and network != tab_name:
            if word[1].lower() == "add":
                hexchat.set_pluginpref("jptab_" + channel, network)
                hexchat.prnt("*\tChannel \00319{0}\00399 on network {1} added to join/part filters".format(channel, network))
                load_jpfilters()
            elif word[1].lower() == "remove":
                hexchat.del_pluginpref("jptab_" + channel)
                hexchat.prnt("*\tChannel \00319{0}\00399 on network {1} removed from joint/part filters".format(channel, network))
                load_jpfilters()
            else:
                hexchat.prnt("Usage: /jptab [add|remove] channel")

        elif word[1].lower() == "list" and word[2].lower() == "filters":
            if len(network_lst) > 0:
                network_filters = ", ".join(network_lst)
                hexchat.prnt("*\tYour join/part network filters are: {}".format(network_filters))
            if len(channel_lst) > 0:
                channel_filters_lst = []
                for channel in channel_lst:
                    network = get_network(channel)
                    channel_filters_lst.append(channel + "/" + network)
                channel_filters = ", ".join(channel_filters_lst)
                hexchat.prnt("*\tYour join/part channel filters are: {}".format(channel_filters))
            if len(network_lst) < 1 and len(channel_lst) < 1:
                hexchat.prnt("*\tYou are not filtering join/part messages on any network or channel")

        else:
            hexchat.prnt("Usage: /jptab [add|remove] [network|channel]\n\t       /jptab list filters")

    else:
        hexchat.prnt("Usage: /jptab [add|remove] [network|channel]\n\t       /jptab list filters")

    return hexchat.EAT_ALL

# for filtering by network
network_lst = []

# for filtering by channel on the current network
channel_lst = []
chan_net_lst = []

def load_jpfilters():
    global network_lst
    global channel_lst
    global chan_net_lst
    # reset the lists so that the script doesn't have to be reloaded
    network_lst = []
    channel_lst = []
    chan_net_lst = []
    for pref in hexchat.list_pluginpref():
        if pref[:6] == "jptab_":
            if pref[6] == "#":
                channel = pref[6:]
                network = get_network(channel)
                channel_lst.append(channel)
                chan_net_lst.append(network)
            else:
                network = pref[6:]
                network_lst.append(network)

def pref_check():
    if hexchat.get_info("network") in network_lst:
        return True
    elif hexchat.get_info("channel") in channel_lst and hexchat.get_info("network") in chan_net_lst:
        return True
    else:
        return False

def jpfilter_cb(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    jp_context = hexchat.find_context(channel=tab_name)

    if pref_check():

        if userdata == "Join":
            jp_context.prnt("{0} \00323*\t{1} ({2}) has joined".format(channel, word[0], word[2]))

        elif userdata == "Part":
            jp_context.prnt("{0} \00324*\t{1} ({2}) has left".format(channel, word[0], word[1]))

        elif userdata == "Quit":
            if len(word) > 2:
                jp_context.prnt("{0} \00324*\t{1} has quit ({2})".format(channel, word[0], word[1]))
            else:
                jp_context.prnt("{0} \00324*\t{1} has quit ()".format(channel, word[0]))

        return hexchat.EAT_ALL

    else:
        # print join/part messages normally for all other servers
        return hexchat.EAT_NONE

def unload_callback(userdata):
    # find the join/part tab and close it
    for chan in hexchat.get_list("channels"):
        if chan.type == 1 and chan.channel == tab_name:
            jp_context = hexchat.find_context(channel=tab_name)
            jp_context.command("CLOSE")
    hexchat.prnt(__module_name__ + " version " + __module_version__ + " unloaded.")

hexchat.hook_command("jptab", jptab_pref, help="Filter joins/parts/quits for a network or channel:\n \
\t  /jptab [add|remove] [network|channel]\n \
\t  To list your current filters:\n \
\t  /jptab list filters")
hexchat.hook_print("Join", jpfilter_cb, "Join")
hexchat.hook_print("Part", jpfilter_cb, "Part")
hexchat.hook_print("Quit", jpfilter_cb, "Quit")
hexchat.hook_unload(unload_callback)
load_jpfilters()

hexchat.command("NEWSERVER -noconnect {0}".format(tab_name))
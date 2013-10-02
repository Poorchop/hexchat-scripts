Join/Part Tab
=============
This script aggregates all join, part, and quit mesages from a user-defined list of servers and/or channels and places them in a new tab. The name of the channel from where the join/part/quit event originated is displayed before each join/part/quit message.

Usage:
======
If you want joins/parts/quits to be filtered for a particular server, add it to "host_list". You must add the name of the actual host to which you are connected (chat.freenode.net, irc.mozilla.org, ...) You can double check the name of the host by clicking on a server tab and entering this into the text box:

    /py exec import hexchat; print(hexchat.get_info("host"))

Then add the resulting string to "host_list", save the script, and reload it:

    host_list = ["irc.twitch.tv", "chat.freenode.net", "irc.mozilla.org", ]

You can also filter by channel. Add the name of the channel you wish to filter to "channel_list", save, and reload:
    
    channel_list = ["##linux", "#hexchat", ]

Notes:
======
Most of this script is just Arnavion's [highlight.py] (https://github.com/Arnavion/random/blob/master/hexchat/highlight.py) script and Wardje's [highlightlog.py] (https://github.com/Wardje/xchat-scripts/blob/master/highlightlog.py) script with some words changed around, so most credit goes to them.
Join/Part Tab
=============
This script aggregates all join and part mesages from a user-defined list of servers and places them in a new tab. The name of the channel from where the join/part event originated is displayed before each join/part message.

Usage:
======
If you want joins/parts to be filtered for a particular server, add it to "host_list". You must add the name of the actual host to which you are connected (chat.freenode.net, irc.mozilla.org, ...) You can double check the name of the host by clicking on a server tab and entering this into the text box:

  /py exec import hexchat; print(hexchat.get_info("host"))

Then add the resulting string to "host_list":

  host_list = ["irc.twitch.tv", "chat.freenode.net", "irc.mozilla.org"]

Notes:
======
Most of this script is just Arnavion's [highlight.py] (https://github.com/Arnavion/random/blob/master/hexchat/highlight.py) script with some words changed around, so most credit goes to him.
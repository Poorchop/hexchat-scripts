Join/Part Tab
-------------
This script aggregates all join, part, and quit mesages from a user-defined list of servers and/or channels and places them in a new tab. The name of the channel from where the join/part/quit event originated is displayed before each join/part/quit message.

Usage:
------
You can customize the name of the filter tab by setting `tab_name = ""` to whatever you like. Place your desired name between the quotes.

#### To filter a channel:
* Make the channel you wish to filter the active tab
* `/jptab add channel`
You will see a message that the current activated channel under the current network has been added to the filter list.

#### To filter an entire network:
* Click on the network tab OR on any of the channel tabs under the network you wish to filter
* `/jptab add network`
You will see a message that the current network has been added to the filter list. All channels under this network will have their join/part/quit messages filtered and moved to the filter tab.

#### To remove a channel or network filter:
* Activate the desired channel or network as described above
* For a channel:
    * `/jptab remove channel`
* For a network:
    * `/jptab remove network`
If executed properly, you will see a message that the channel/network has been removed from the filter list.

Notes:
------
This script was made possible due to templates provided by [Arnavion's] (https://github.com/Arnavion), [Wardje's] (https://github.com/Wardje), and [TingPing's] (https://github.com/TingPing) scripts, and with help from [Farow] (https://github.com/Farow), so I'd like to thank them here.
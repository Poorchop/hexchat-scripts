### hexchat-scripts
This repository includes my own scripts as well forks and backups of scripts made by others.
Some of my scripts are still a work in progress. Please let me know if you find any issues.
Many of these scripts were made possible with help or with templates from
[TingPing] (https://github.com/TingPing), [Farow] (https://github.com/Farow),
[Arnavion] (https://github.com/Arnavion), [GermainZ] (https://github.com/GermainZ), and others.

***

#### [Arnavion-scripts] (./Arnavion-scripts)
Clone of Arnavion's script repository. His Royal Highness requests that
absolutely nobody contact him about these scripts for any reason whatsoever.
I take no credit for any of these scripts and as the original repository did not
include a license, their licensing is technically handled by the
[GitHub Terms of Service] (https://help.github.com/articles/github-terms-of-service#f-copyright-and-content-ownership).

#### [adfilter.py] (adfilter.py)
Move common fserve advertisements to a separate tab

To those coming from mIRC, this is meant to to partially replicate the ad-related functionality of
[DukeLupus's dlFilter script] (http://dukelupus.com/dlfilter).

*__Usage:__*	
You only need to modify `channels = []` for this script to work.
See the script comment if you need instructions on how to add a channel to the filter list.

#### [dcc-spam.py] (dcc-spam.py)
*Untested*: This script should theoretically detect DCC spammers and automatically add them to ignore.
Since I haven't tested it, expect things to be broken. Currently, it only ignores people trying to
repeatedly send the same file within a five second period.

#### [follow.py] (follow.py)
Format messages from specific users to make them easier to follow

*__Usage:__*	
/follow &lt;nick&gt;	
/unfollow &lt;nick&gt;

#### [hexchat-livestreamer.py] (hexchat-livestreamer.py)
Automatically launch a Twitch.TV stream via Livestreamer when the corresponding channel is joined in HexChat.
[Livestreamer] (http://livestreamer.tanuki.se/) must be installed for this script to work correctly.

*__Usage:__*	
Follow the [guide] (http://help.twitch.tv/customer/portal/articles/1302780-twitch-irc#Hexchat%20Guide) for connecting
to Twitch chat with HexChat, then join a channel to launch the corresponding stream with Livestreamer.

You can alternately type `/livestreamer <#channel> <quality>` to manually launch a stream.

#### [joinparttab.py] (joinparttab.py)
This script aggregates all join, part, and quit mesages from a user-defined list of servers and/or channels and places them in a new tab.
The name of the channel from where the join/part/quit event originated is displayed before each join/part/quit message.

*__Usage:__*	
You can customize the name of the filter tab by setting `tab_name = ""` to whatever you like.
Place your desired name between the quotes. You can view the available commands for this script by typing `/help jptab`.

**To filter a channel:**	
* Make the channel you wish to filter the active tab
* `/jptab add channel`

You will see a message that the current activated channel under the current network has been added to the filter list.

**To filter an entire network:**	
* Click on the network tab OR on any of the channel tabs under the network you wish to filter
* `/jptab add network`

You will see a message that the current network has been added to the filter list.
All channels under this network will have their join/part/quit messages filtered and moved to the filter tab.

**To remove a channel or network filter:**	
* Activate the desired channel or network as described above
* For a channel:
    * `/jptab remove channel`
* For a network:
    * `/jptab remove network`
    
If executed properly, you will see a message that the channel/network has been removed from the filter list.

**To view your current filters:**	
* `/jptab list filters`

#### [link-title.py] (link-title.py)
Display website titles above links that are pasted in chat

Plays nicely with [get-youtube-video-info.py] (https://github.com/demialucard/xchat-scripts/blob/master/get-youtube-video-info.py)
(some message formatting also taken from that script)

#### [nick2server.py] (nick2server.py)
Remove nick change messages from channels and place them in the server tab instead

Inspired by notice2server.pl from the legendary [Farow] (https://github.com/Farow)

#### [nickspy.py] (nickspy.py)
Colorize a channel name in the channel tree when certain users speak in said channel

*__Usage:__*	
Add nicknames for spying on to `nicknames = []`. Nicknames should be in quotes and separated by commas:

`nicknames = ["nick1", "nick2", "nick3"]`

#### [pyglatin.py] (pyglatin.py)
This script is based on the PygLatin Python exercise written by Kate Lockwood:
* If a word begins with a vowel, "ay" is appended to the end of the word.
* If a word instead begins with a consonant, the first letter of the word is moved to the end, and the result is appended with "ay".

*__Usage:__*	
/pyg &lt;message&gt;

#### [requestfilter.py] (requestfilter.py)
Move search requests (@find, @search, @seek, etc.) and fserve file requests to a separate tab

To those coming from mIRC, this is meant to to partially replicate the request-related functionality of
[DukeLupus's dlFilter script] (http://dukelupus.com/dlfilter).

This script is meant to complement [adfilter.py] (adfilter.py),
but they can be used independently of each other.

*__Usage:__*	
You only need to modify `channels = []` for this script to work.
See the script comment if you need instructions on how to add a channel to the filter list.

#### [shortnicks.py] (shortnicks.py)
Automatically truncate nicknames beyond a user-defined length

*__Usage:__*	
See script comment for instructions

#### [twitch-autoemote.py] (twitch-autoemote.py)
Automatically formats TwitchTV emotes with proper capitalization

Use [TingPing's twitch.py script] (https://github.com/TingPing/plugins/blob/master/HexChat/twitch.py)
for a more comprehensive Twitch experience.

*__Usage:__*	
Emotes are formatted with proper capitalization as you type.
This only modifies your text when a Twitch IRC channel is in focus.
Therefore, this script is essentially a twitch-specific auto-replace tool.

Example: "Hello kappa frankerz" is automatically converted to "Hello Kappa FrankerZ" as you type.

### Installation:
Place "script.py" in your HexChat addons folder:

* Windows:
    * `%APPDATA%\HexChat\addons`
* Linux:
    * `~/.config/hexchat/addons`

The HexChat Python plugin interface is required.

### Notes:
All scripts are under the [MIT license] (./license) unless otherwise stated.

I highly recommend checking out [Farow's readme] (https://github.com/Farow/hexchat-scripts).
Both he and [TingPing] (https://github.com/TingPing/plugins) have really useful scripts.
Also check out my starred repositories to find additional scripts that I might have not yet listed below.

Here are some links in addition to Farow's:

#### GitHub
* [ChaozZBubi] (https://github.com/ChaozZBubi/tools)
* [Chuong Ngo] (https://github.com/cngo-github/xchat-translator)
* [demialucard] (https://github.com/demialucard/xchat-scripts)
(see [here] (https://github.com/PoorDog/xchat-scripts/blob/master/get-youtube-video-info.py) for Python 3 support)
* [GermainZ] (https://github.com/GermainZ/HexChat-Scripts)
* [iceTwy] (https://github.com/iceTwy/xchat-deadbeef)
* [logicplace] (https://github.com/logicplace/xchat-plugins)
* [Phr33d0m] (https://github.com/Phr33d0m/Random)
* [Wardje] (https://github.com/Wardje/xchat-scripts)

#### Elsewhere
* [Chryyz] (https://bitbucket.org/Chryyz/hexchat-scripts/src)
* [Dan Boklöv-Palovaara] (http://dev.wh00s.net/index.php?py)
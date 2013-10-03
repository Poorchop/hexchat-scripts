twitch-autoemote
================
Automatically formats twitch.tv emotes with proper capitalization

Usage:
======
Emotes are automatically formatted only for text sent to channels on twitch.tv IRC.

Example: "Hello kappa frankerz" is automatically converted to "Hello Kappa FrankerZ" after you send your message, and the corresponding emotes are displayed in the web chat.

You can add emotes for the current session via the following line:

    /twitch add <alias> <emote>
    
For example, by doing "/twitch add newemote NewEmote", "newemote" will be automatically formatted to "NewEmote" for your current session. If you want your emotes to persist across sessions, you must manually edit the script.

To view a list of emotes, including those for the current session, enter the follow line:

    /twitch emotes

Notes:
======
This script is an experimental work in progress. Use [TingPing's twitch.py script] (https://github.com/TingPing/plugins/blob/master/HexChat/twitch.py) for a more comprehensive twitch experience.

A very big thank you to [TingPing] (https://github.com/TingPing) and [GermainZ] (https://github.com/GermainZ) for help with, syntax, implementation, and suggestions.
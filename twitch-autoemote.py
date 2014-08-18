# coding=utf-8

import hexchat
import os

__module_name__ = "Twitch Emote Autoformat"
__module_author__ = "Poorchop"
__module_version__ = "0.7"
__module_description__ = "Automatically format TwitchTV emote names with proper capitalization"
# TODO: cross platform support
# TODO: emote unicode character support
# TODO: only load subscriber emotes for subscribed/specified channels

# change this value to False if you do not wish to use subscriber emotes
allow_sub_emotes = True

events = ("Channel Message", "Channel Msg Hilight",
          "Channel Action", "Channel Action Hilight",
          "Your Message")
edited = False

# emote names taken from: http://twitchemotes.com/
# list last updated August 18, 2014
emote_dict = {'4head': '4Head',
              'arsonnosexy': 'ArsonNoSexy',
              'asianglow': 'AsianGlow',
              'atgl': 'AtGL',
              'ativy': 'AtIvy',
              'atww': 'AtWW',
              'bcwarrior': 'BCWarrior',
              'bort': 'BORT',
              'batchest': 'BatChest',
              'biblethump': 'BibleThump',
              'bigbrother': 'BigBrother',
              'bionicbunion': 'BionicBunion',
              'blargnaunt': 'BlargNaut',
              'bloodtrail': 'BloodTrail',
              'brainslug': 'BrainSlug',
              'brokeback': 'BrokeBack',
              'cougarhunt': 'CougarHunt',
              'daesuppy': 'DAESuppy',
              'dbstyle': 'DBstyle',
              'dansgame': 'DansGame',
              'datsheffy': 'DatSheffy',
              'dogface': 'DogFace',
              'eagleeye': 'EagleEye',
              'elegiggle': 'EleGiggle',
              'evilfetus': 'EvilFetus',
              'fpsmarksman': 'FPSMarksman',
              'fungineer': 'FUNgineer',
              'failfish': 'FailFish',
              'frankerz': 'FrankerZ',
              'freakinstinkin': 'FreakinStinkin',
              'fuzzyotteroo': 'FuzzyOtterOO',
              'gasjoker': 'GasJoker',
              'gingerpower': 'GingerPower',
              'grammarking': 'GrammarKing',
              'hassaanchop': 'HassaanChop',
              'hassanchop': 'HassanChop',
              'hotpokket': 'HotPokket',
              'itsboshytime': 'ItsBoshyTime',
              'jkanstyle': 'JKanStyle',
              'jebaited': 'Jebaited',
              'joncarnage': 'JonCarnage',
              'kapow': 'KAPOW',
              'kzassault': 'KZassault',
              'kzcover': 'KZcover',
              'kzguerilla': 'KZguerilla',
              'kzhelghast': 'KZhelghast',
              'kzowl': 'KZowl',
              'kzskull': 'KZskull',
              'kappa': 'Kappa',
              'keepo': 'Keepo',
              'kevinturtle': 'KevinTurtle',
              'kippa': 'Kippa',
              'kreygasm': 'Kreygasm',
              'mvgame': 'MVGame',
              'mechasupes': 'MechaSupes',
              'mrdestructoid': 'MrDestructoid',
              'nightbat': 'NightBat',
              'ninjatroll': 'NinjaTroll',
              'nonospot': 'NoNoSpot',
              'omgscoots': 'OMGScoots',
              'onehand': 'OneHand',
              'opieop': 'OpieOP',
              'optimizeprime': 'OptimizePrime',
              'pjharley': 'PJHarley',
              'pjsalt': 'PJSalt',
              'pmstwin': 'PMSTwin',
              'panicvis': 'PanicVis',
              'pazpazowitz': 'PazPazowitz',
              'peopleschamp': 'PeoplesChamp',
              'picomause': 'PicoMause',
              'pipehype': 'PipeHype',
              'pogchamp': 'PogChamp',
              'poooound': 'Poooound',
              'punchtrees': 'PunchTrees',
              'ralpherz': 'RalpherZ',
              'redcoat': 'RedCoat',
              'residentsleeper': 'ResidentSleeper',
              'ritzmitz': 'RitzMitz',
              'rulefive': 'RuleFive',
              'smorc': 'SMOrc',
              'smskull': 'SMSkull',
              'ssssss': 'SSSsss',
              'shazbotstix': 'ShazBotstix',
              'shazam': "Shazam",
              'sobayed': 'SoBayed',
              'sonnerlater': 'SoonerLater',
              'srihead': 'SriHead',
              'stonelightning': 'StoneLightning',
              'strawbeary': 'StrawBeary',
              'supervinlin': 'SuperVinlin',
              'swiftrage': 'SwiftRage',
              'tf2john': 'TF2John',
              'tehfunrun': 'TehFunrun',
              'theringer': 'TheRinger',
              'thetarfu': 'TheTarFu',
              'thething': 'TheThing',
              'thunbeast': 'ThunBeast',
              'tinyface': 'TinyFace',
              'toospicy': 'TooSpicy',
              'trihard': 'TriHard',
              'uleetbackup': 'UleetBackup',
              'unsane': 'UnSane',
              'unclenox': 'UncleNox',
              'volcania': 'Volcania',
              'wtruck': 'WTRuck',
              'wholewheat': 'WholeWheat',
              'winwaker': 'WinWaker',
              'youwhy': 'YouWHY',
              'aneleanele': 'aneleanele',
              'noscope420': 'noScope420',
              'shazamicon': 'shazamicon'}

if allow_sub_emotes:
    file_path = os.path.join(hexchat.get_info("configdir"),
                             "addons", "twitch-sub-emotes.txt")

    if os.path.exists(file_path):
        f = open(file_path, "r")
        for line in f:
            stripped_emote = line.replace("\n", "")
            lowercase_emote = stripped_emote.lower()
            emote_dict[lowercase_emote] = stripped_emote
        f.close()
    else:
        print("*** Subscriber emote list not found! Download it at "
              "https://raw.githubusercontent.com/Poorchop/hexchat-scripts/master/twitch-sub-emotes.txt, "
              "place it in your HexChat addons folder, and then reload this script to use subscriber emotes. ***")


def is_twitch():
    server = hexchat.get_info("host")
    if server and "twitch.tv" in server:
        return True
    else:
        return False


def keypress_cb(word, word_eol, userdata):
    key = word[0]
    mod = word[1]

    #                  a    ctrl          backspace
    if (key, mod) == ("97", "4") or key == "65288":
        return

    if is_twitch():
        msg = hexchat.get_info("inputbox")

        if msg:
            split_words = msg.split(" ")

            for w in split_words:
                if w.lower() in emote_dict:
                    split_words[split_words.index(w)] = emote_dict[w.lower()]

            new_msg = " ".join(split_words)
            hexchat.command("SETTEXT {}".format(new_msg))
            hexchat.command("SETCURSOR {}".format(len(new_msg)))


def emote_cb(word, word_eol, event):
    word = [(word[i] if len(word) > i else "") for i in range(4)]
    global edited

    if edited:
        return

    if is_twitch():
        word[1] = word[1] \
            .replace(":)", "😊") \
            .replace(":(", "☹") \
            .replace(":z", "😴") \
            .replace("B)", "😎") \
            .replace(";)", "😉") \
            .replace(";p", "😜") \
            .replace(":p", "😛") \
            .replace(":D", "😄") \
            .replace(">(", "😠") \
            .replace("<3", "♥") \
            .replace("BionicBunion", "😺") \
            .replace("FrankerZ", "🐶") \
            .replace("ItsBoshyTime", "⚠") \
            .replace("Kappa", "😏") \
            .replace("KZskull", "💀")

        edited = True
        hexchat.emit_print(event, *word)
        edited = False

        return hexchat.EAT_ALL


hexchat.hook_print("Key Press", keypress_cb)
for event in events:
    hexchat.hook_print(event, emote_cb, event, priority=hexchat.PRI_HIGH)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

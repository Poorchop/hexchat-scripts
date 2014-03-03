# coding=utf-8

import hexchat

__module_name__ = "Twitch Emote Autoformat"
__module_author__ = "PDog"
__module_version__ = "0.6"
__module_description__ = "Automatically format twitch.tv emote names with proper capitalization"

events = ("Channel Message", "Channel Msg Hilight",
          "Channel Action", "Channel Action Hilight",
          "Your Message")
edited = False

# emote names taken from: http://twitchemotes.com/
# list last updated Sept 20, 2013
emote_dict = {'4head' : '4Head', 
              'arsonnosexy' : 'ArsonNoSexy', 
              'asianglow' : 'AsianGlow', 
              'bcwarrior' : 'BCWarrior', 
              'bort' : 'BORT', 
              'batchest' : 'BatChest', 
              'biblethump' : 'BibleThump', 
              'bigbrother' : 'BigBrother', 
              'bionicbunion' : 'BionicBunion', 
              'blargnaunt' : 'BlargNaut', 
              'bloodtrail' : 'BloodTrail', 
              'brainslug' : 'BrainSlug', 
              'brokeback' : 'BrokeBack', 
              'cougarhunt' : 'CougarHunt', 
              'daesuppy' : 'DAESuppy', 
              'dbstyle' : 'DBstyle', 
              'dansgame' : 'DansGame', 
              'datsheffy' : 'DatSheffy', 
              'dogface' : 'DogFace', 
              'eagleeye' : 'EagleEye', 
              'evilfetus' : 'EvilFetus', 
              'fpsmarksman' : 'FPSMarksman', 
              'fungineer' : 'FUNgineer', 
              'failfish' : 'FailFish', 
              'frankerz' : 'FrankerZ', 
              'freakinstinkin' : 'FreakinStinkin', 
              'fuzzyotteroo' : 'FuzzyOtterOO', 
              'gingerpower' : 'GingerPower', 
              'hassanchop' : 'HassanChop', 
              'hotpokket' : 'HotPokket', 
              'itsboshytime' : 'ItsBoshyTime', 
              'jkanstyle' : 'JKanStyle', 
              'jebaited' : 'Jebaited', 
              'joncarnage' : 'JonCarnage', 
              'kappa' : 'Kappa', 
              'keepo' : 'Keepo', 
              'kevinturtle' : 'KevinTurtle', 
              'kippa' : 'Kippa', 
              'kreygasm' : 'Kreygasm', 
              'mvgame' : 'MVGame', 
              'mrdestructoid' : 'MrDestructoid', 
              'ninjatroll' : 'NinjaTroll', 
              'nonospot' : 'NoNoSpot', 
              'omgscoots' : 'OMGScoots', 
              'onehand' : 'OneHand', 
              'opieop' : 'OpieOP', 
              'optimizeprime' : 'OptimizePrime', 
              'pjsalt' : 'PJSalt', 
              'pmstwin' : 'PMSTwin', 
              'pazpazowitz' : 'PazPazowitz', 
              'picomause' : 'PicoMause', 
              'pogchamp' : 'PogChamp', 
              'poooound' : 'Poooound', 
              'punchtrees' : 'PunchTrees', 
              'ralpherz' : 'RalpherZ', 
              'redcoat' : 'RedCoat', 
              'residentsleeper' : 'ResidentSleeper', 
              'rulefive' : 'RuleFive', 
              'smorc' : 'SMOrc', 
              'smskull' : 'SMSkull', 
              'ssssss' : 'SSSsss', 
              'shazbotstix' : 'ShazBotstix', 
              'sobayed' : 'SoBayed', 
              'sonnerlater' : 'SoonerLater', 
              'stonelightning' : 'StoneLightning', 
              'strawbeary' : 'StrawBeary', 
              'supervinlin' : 'SuperVinlin', 
              'swiftrage' : 'SwiftRage', 
              'tf2john' : 'TF2John', 
              'tehfunrun' : 'TehFunrun', 
              'theringer' : 'TheRinger', 
              'therarfu' : 'TheTarFu', 
              'thunbeast' : 'ThunBeast', 
              'tinyface' : 'TinyFace', 
              'toospicy' : 'TooSpicy', 
              'trihard' : 'TriHard', 
              'uleetbackup' : 'UleetBackup', 
              'unsane' : 'UnSane', 
              'volcania' : 'Volcania', 
              'wtruck' : 'WTRuck', 
              'wholewheat' : 'WholeWheat', 
              'winwaker' : 'WinWaker'}

def is_twitch():
    if "twitch.tv" in hexchat.get_info("host"):
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
            .replace(":)", "☺") \
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

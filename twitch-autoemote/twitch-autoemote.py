import hexchat

__module_name__ = "Twitch Emote Autoformat"
__module_author__ = "PoorDog"
__module_version__ = "0.2.1"
__module_description__ = "Automatically format twitch.tv emote names with proper capitalization"

hexchat.prnt (__module_name__ + " version " + __module_version__ + " loaded.")

twitch_help = "Twitch: To add an emote for current session:\n \
  /twitch add <alias> <emote>\n \
  Ex: /twitch add frankerz FrankerZ\n \
  To list your current emotes:\n \
  /twitch emotes"
  # add info for mod commands when combining with TingPing's twitch.py script

# emote_dict is customizable. You can easily add or remove rules to your liking. Subscriber-only emotes are not included in the default list, so these can appended as necessary.
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
              'ralpherz' : 'RalpherZ', 'redcoat' : 'RedCoat', 
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

unedited = True

def is_twitch():
    if "twitch.tv" in hexchat.get_info("server"):
        return True
    else: 
        return False

def twitch_cb(word, word_eol, userdata):
    if len(word) > 1:
        cmd = word[1].lower()

        if cmd == "add" and len(word) == 4:
            emote_dict.update({word[2] : word[3]})
            hexchat.prnt("\00319\002{0}\002\00399 with alias \00320\002{1}\002\00399 successfully added to emote list!".format(word[3], word[2]))
        elif cmd == "emotes":
            emote_lst = []
            for key in emote_dict:
                emote_lst.append(emote_dict[key])
            emote_lst.sort()
            hexchat.prnt(" ".join(emote_lst))
        # Uncomment elif block below when combining with TingPing's twitch.py script
        # elif cmd == "commands":
        #     for command in commands:
        #         print command, 
        else:
            hexchat.command("help twitch")
            return hexchat.EAT_ALL

    else:
        hexchat.command("help twitch")
        return hexchat.EAT_ALL
    
def emote_cb(word, word_eol, userdata):
    global unedited

    if is_twitch() and unedited and len(word) > 0:
        unedited = False
        split_words = word_eol[0].split(" ")
        split_lower = [x.lower() for x in split_words]

        for y in range(0, len(split_lower)):
            for z in emote_dict:
                if split_lower[y] == z:
                    split_words[y] = emote_dict[z]

        new_words = " ".join(split_words)
        hexchat.command("say {}".format(new_words))
        return hexchat.EAT_ALL

    else:
        unedited = True
        return hexchat.EAT_NONE

hexchat.hook_command("", emote_cb, priority=hexchat.PRI_HIGH)
hexchat.hook_command("twitch", twitch_cb, help=twitch_help)
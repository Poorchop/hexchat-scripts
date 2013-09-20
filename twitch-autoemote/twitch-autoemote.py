import hexchat

__module_name__ = "twitch-autoemote"
__module_author__ = "PoorDog"
__module_version__ = "0.1"
__module_description__ = "Automatically format twitch.tv emote names with proper capitalization"

hexchat.prnt (__module_name__ + " version " + __module_version__ + " loaded.")

# emote_dict is customizable. You can easily add or remove rules to your liking. Subscriber-only emotes are not included in the default list, so these can appended as necessary.
emote_dict = {'4head' : '4Head', 'arsonnosexy' : 'ArsonNoSexy', 'asianglow' : 'AsianGlow', 'bcwarrior' : 'BCWarrior', 'bort' : 'BORT', 'batchest' : 'BatChest', 'biblethump' : 'BibleThump', 'bigbrother' : 'BigBrother', 'bionicbunion' : 'BionicBunion', 'blargnaunt' : 'BlargNaut', 'bloodtrail' : 'BloodTrail', 'brainslug' : 'BrainSlug', 'brokeback' : 'BrokeBack', 'cougarhunt' : 'CougarHunt', 'daesuppy' : 'DAESuppy', 'dbstyle' : 'DBstyle', 'dansgame' : 'DansGame', 'datsheffy' : 'DatSheffy', 'dogface' : 'DogFace', 'eagleeye' : 'EagleEye', 'evilfetus' : 'EvilFetus', 'fpsmarksman' : 'FPSMarksman', 'fungineer' : 'FUNgineer', 'failfish' : 'FailFish', 'frankerz' : 'FrankerZ', 'freakinstinkin' : 'FreakinStinkin', 'fuzzyotteroo' : 'FuzzyOtterOO', 'gingerpower' : 'GingerPower', 'hassanchop' : 'HassanChop', 'hotpokket' : 'HotPokket', 'itsboshytime' : 'ItsBoshyTime', 'jkanstyle' : 'JKanStyle', 'jebaited' : 'Jebaited', 'joncarnage' : 'JonCarnage', 'kappa' : 'Kappa', 'keepo' : 'Keepo', 'kevinturtle' : 'KevinTurtle', 'kippa' : 'Kippa', 'kreygasm' : 'Kreygasm', 'mvgame' : 'MVGame', 'mrdestructoid' : 'MrDestructoid', 'ninjatroll' : 'NinjaTroll', 'nonospot' : 'NoNoSpot', 'omgscoots' : 'OMGScoots', 'onehand' : 'OneHand', 'opieop' : 'OpieOP', 'optimizeprime' : 'OptimizePrime', 'pjsalt' : 'PJSalt', 'pmstwin' : 'PMSTwin', 'pazpazowitz' : 'PazPazowitz', 'picomause' : 'PicoMause', 'pogchamp' : 'PogChamp', 'poooound' : 'Poooound', 'punchtrees' : 'PunchTrees', 'ralpherz' : 'RalpherZ', 'redcoat' : 'RedCoat', 'residentsleeper' : 'ResidentSleeper', 'rulefive' : 'RuleFive', 'smorc' : 'SMOrc', 'smskull' : 'SMSkull', 'ssssss' : 'SSSsss', 'shazbotstix' : 'ShazBotstix', 'sobayed' : 'SoBayed', 'sonnerlater' : 'SoonerLater', 'stonelightning' : 'StoneLightning', 'strawbeary' : 'StrawBeary', 'supervinlin' : 'SuperVinlin', 'swiftrage' : 'SwiftRage', 'tf2john' : 'TF2John', 'tehfunrun' : 'TehFunrun', 'theringer' : 'TheRinger', 'therarfu' : 'TheTarFu', 'thunbeast' : 'ThunBeast', 'tinyface' : 'TinyFace', 'toospicy' : 'TooSpicy', 'trihard' : 'TriHard', 'uleetbackup' : 'UleetBackup', 'unsane' : 'UnSane', 'volcania' : 'Volcania', 'wtruck' : 'WTRuck', 'wholewheat' : 'WholeWheat', 'winwaker' : 'WinWaker'}

i = 1

def is_twitch():
    if 'twitch.tv' in hexchat.get_info('server'):
        return True
    else: 
        return False

def auto_caps(word, word_eol, userdata):
    global i
    if is_twitch() and len(word) > 0 and i == 1:
        i -= 1
        split_words = word_eol[0].split(" ")
        split_lower = [x.lower() for x in split_words]

        for y in range(0, len(split_lower)):
            for z in emote_dict:
                if split_lower[y] == z:
                    split_words[y] = emote_dict[z]

        new_words = " ".join(split_words)
        hexchat.command("say %s" % (new_words))
        return hexchat.EAT_ALL

    else:
        i = 1

hexchat.hook_command("", auto_caps)

import hexchat

__module_name__ = "Twitch Emote Autoformat"
__module_author__ = "PDog"
__module_version__ = "0.4"
__module_description__ = "Automatically format twitch.tv emote names with proper capitalization"

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

moved = False

def is_twitch():
    if "twitch.tv" in hexchat.get_info("host"):
        return True
    else: 
        return False
    
def emote_cb(word, word_eol, userdata):
    global moved

    if moved:
        return

    if is_twitch():
        for w in word:
            if w.lower() in emote_dict:
                word[word.index(w)] = emote_dict[w.lower()]

        new_msg = " ".join(word)

        moved = True
        hexchat.command("SAY {0}".format(new_msg))
        moved = False

        return hexchat.EAT_ALL

hexchat.hook_command("", emote_cb, priority=hexchat.PRI_HIGH)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

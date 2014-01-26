import hexchat

__module_name__ = "PygLatin"
__module_author__ = "PDog"
__module_version__ = "2"
__module_description__ = "Convert text to PygLatin"

pyg = "ay"
vowels = ["a", "e", "i", "o", "u"]

def pyglatin_cb(word, word_eol, userdata):
	if len(word) < 2:
		hexchat.prnt("-\00322PygLatin\00399-\tUsage: /pyg <message>")
	else:
		word.remove(word[0])
		for w in word:
			first = w[0]
			spliced = w[1:]
			
			if first.lower() in vowels:
				word[word.index(w)] = w + pyg
			else:
				word[word.index(w)] = spliced + first + pyg
	
		new_msg = " ".join(word)
		hexchat.command("SAY {0}".format(new_msg))
		return hexchat.EAT_ALL

hexchat.hook_command("PYG", pyglatin_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")
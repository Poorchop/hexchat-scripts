# Usage: /pyg <message>

import xchat

__module_name__ = "PygLatin"
__module_author__ = "PoorDog"
__module_version__ = "1.0"
__module_description__ = "Convert text to PygLatin"

print (__module_name__, "version", __module_version__, "loaded.")

pyg = "ay"

def pyglatin(word, word_eol, userdata):
    split_words = word_eol[1].split(" ")
    i = 0

    for x in split_words: # this loop modifies the split_words list by changing all individual words to the PygLatin form
        if len(split_words) > 0 and x.isalpha(): # checks to see if any characters have been entered and that they are all letters
            first = x[0]
            spliced = x[1:]
            if first == "a" or first == "A" or first == "e" or first == "E" or first == "i" or first == "I" or first == "o" or first == "O" or first == "u" or first == "U":
                split_words[i] = x + pyg
                i += 1
            else:
                split_words[i] = spliced + first + pyg
                i += 1
        else:
            i += 1

    new_str = " ".join(split_words) # concatenation of split_words list with spaces between words
    xchat.command("say %s" % (new_str)) # send translated text to server
    return xchat.EAT_ALL

xchat.hook_command("pyg", pyglatin)

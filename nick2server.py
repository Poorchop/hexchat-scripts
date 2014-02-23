import hexchat

__module_name__ = "Nick to Server Tab"
__module_author__ = "PDog"
__module_version__ = "0.1"
__module_description__ = "Move nick change messages to the server tab"

moved = False

def move_cb(word, word_eol, userdata):
	global moved

	if moved:
                return
                
        for chan in hexchat.get_list("channels"):
                if chan.type == 1 and chan.id == hexchat.get_prefs("id"):
                        network_context = chan.context
				
        moved = True
        network_context.emit_print("Change Nick", word[0], word[1])
        moved = False
		
        return hexchat.EAT_ALL

hexchat.hook_print("Change Nick", move_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

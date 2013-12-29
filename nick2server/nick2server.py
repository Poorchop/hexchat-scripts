import hexchat

__module_name__ = "Nick to Server Tab"
__module_author__ = "PDog"
__module_version__ = "0.0.2"
__module_description__ = "Move nick change messages to the server tab"

moved = False

def move_cb(word, word_eol, event):
	global moved

	if moved:
		return
	
	if event == "Change Nick":
		network_context = hexchat.find_context(channel=hexchat.get_info("network"))
		
		moved = True
		network_context.emit_print("Change Nick", word[0], word[1])
		moved = False
		
		return hexchat.EAT_ALL

hexchat.hook_print("Change Nick", move_cb, "Change Nick")
hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")
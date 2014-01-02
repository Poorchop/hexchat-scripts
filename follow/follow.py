import hexchat

__module_name__ = "Follow"
__module_author__ = "PDog"
__module_version__ = "0.2"
__module_description__ = "Format messages from specific users to make them easier to follow"

userlist = []
edited = False

def follow_cb(word, word_eol, userdata):
	global userlist
	
	if len(word) >= 2 and word[1] not in userlist:
		userlist.append(word[1])
		hexchat.prnt("-\00322Follow\00399-\tYou are now following \002{0}".format(word[1]))
		return hexchat.EAT_ALL

def unfollow_cb(word, word_eol, userdata):
	global userlist
	
	if len(word) >= 2 and word[1] in userlist:
		userlist.remove(word[1])
		hexchat.prnt("-\00322Follow\00399-\tYou have unfollowed \002{0}".format(word[1]))
		return hexchat.EAT_ALL

def format_cb(word, word_eol, event):
	global edited
	
	if edited:
		return
	
	if word[0] in userlist:
		formatted_nick = "\002{0}\002".format(word[0])
		formatted_msg = "\00318{0}".format(word[1])
		
		edited = True
		hexchat.emit_print(event, formatted_nick, formatted_msg)
		edited = False
		
		return hexchat.EAT_ALL
	
hexchat.hook_command("FOLLOW", follow_cb)
hexchat.hook_command("UNFOLLOW", unfollow_cb)
hexchat.hook_print("Channel Message", format_cb, "Channel Message")
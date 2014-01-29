import hexchat

__module_name__ = 'AutoInvite'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('AutoInvite script loaded')

def autoinvite_callback(word, word_eol, user_data):
	channel = word[0]
	
	def invited_callback(word, word_eol, user_data):
		invited_result = hexchat.EAT_NONE
		
		if word[0] == channel:
			hexchat.unhook(invited_hook)
			hexchat.unhook(denied_hook)
			invited_result = hexchat.EAT_HEXCHAT
			hexchat.command('join {0}'.format(channel))
		
		return invited_result
	
	invited_hook = hexchat.hook_print('Invited', invited_callback)
	
	def denied_callback(word, word_eol, user_data):
		if word[1] == 'Permission denied.':
			hexchat.unhook(invited_hook)
			hexchat.unhook(denied_hook)
		
		return hexchat.EAT_NONE
	
	denied_hook = hexchat.hook_print('Notice', denied_callback)
	
	hexchat.command('msg ChanServ invite {0}'.format(channel))
	
	return hexchat.EAT_HEXCHAT

hexchat.hook_print('Invite', autoinvite_callback)

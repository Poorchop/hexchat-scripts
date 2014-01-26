import hexchat
import re

__module_name__ = 'AutoUnban'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('AutoUnban script loaded')

def banned_callback(word, word_eol, user_data):
	channel = word[0]
	
	def notice_callback(word, word_eol, user_data):
		unban_result = hexchat.EAT_NONE
		nickname = hexchat.get_info('nick')
		
		if re.search(r'{0} has been unbanned from {1}\.'.format(nickname, channel), hexchat.strip(word[1])):
			hexchat.unhook(notice_hook)
			unban_result = hexchat.EAT_HEXCHAT
			hexchat.command('join {0}'.format(channel))
		
		elif word[1] == 'Permission denied.':
			hexchat.unhook(notice_hook)
		
		return unban_result
	
	notice_hook = hexchat.hook_print('Notice', notice_callback)
	
	hexchat.command('msg ChanServ unban {0}'.format(channel))
	
	return hexchat.EAT_HEXCHAT

hexchat.hook_print('Banned', banned_callback, priority=hexchat.PRI_HIGHEST)

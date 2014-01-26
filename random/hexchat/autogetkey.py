import hexchat
import re

__module_name__ = 'AutoGetkey'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('AutoGetkey script loaded')

def autogetkey_callback(word, word_eol, user_data):
	channel = word[0]
	
	def getkey_callback(word, word_eol, user_data):
		key = ''
		
		matches = re.match('KEY {0} (.*)$'.format(channel), word[1]) or re.match('Channel \x02{0}\x02 key is: (.*)$'.format(channel), word[1])
		if matches:
			hexchat.unhook(getkey_hook)
			key = matches.group(1)
		
		elif word[1] == 'Access denied.' or word[1] == 'You are not authorized to perform this operation.':
			hexchat.unhook(getkey_hook)
		
		if key:
			hexchat.command('join {0} {1}'.format(channel, key))
	
	getkey_hook = hexchat.hook_print('Notice', getkey_callback)
	
	hexchat.command('msg ChanServ getkey {0}'.format(channel))

hexchat.hook_print('Keyword', autogetkey_callback)

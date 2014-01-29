import hexchat

__module_name__ = 'GreenText'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('GreenText script loaded')

def greentext_callback(word, word_eol, user_data):
	word = [word[i] if len(word) > i else '' for i in range(4)]
	
	result = hexchat.EAT_NONE
	
	if word[1][0] == '>':
		hexchat.emit_print(user_data, word[0], '\003' + '09' + word[1], word[2], word[3])
		result = hexchat.EAT_ALL
	
	return result

hexchat.hook_print('Channel Message', greentext_callback, 'Channel Message')
hexchat.hook_print('Your Message', greentext_callback, 'Your Message')

import hexchat

__module_name__ = 'Highlight Logger'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('Highlight Logger loaded')

tab_name = '(Highlights)'

def highlight_callback(word, word_eol, user_data):
	global tab_name
	
	word = [(word[i] if len(word) > i else '') for i in range(4)]
	
	highlight_context = hexchat.find_context(channel=tab_name)
	if highlight_context is None:
		create_highlighttab()
		highlight_context = hexchat.find_context(channel=tab_name)
	
	channel = hexchat.get_info('channel')
	
	if user_data == 'Channel Msg Hilight':
		highlight_context.emit_print('Channel Message', channel, '<{3}{2}{0}> {1}'.format(word[0], word[1], word[2], word[3]), '', '')
	elif user_data == 'Channel Action Hilight':
		highlight_context.emit_print('Channel Action', channel, '{3}{2}{0} {1}'.format(word[0], word[1], word[2], word[3]), '', '')
	
	return hexchat.EAT_NONE

def create_highlighttab():
	global tab_name
	
	hexchat.command('query {0}'.format(tab_name))

create_highlighttab()

hexchat.hook_print('Channel Msg Hilight', highlight_callback, 'Channel Msg Hilight')
hexchat.hook_print('Channel Action Hilight', highlight_callback, 'Channel Action Hilight')

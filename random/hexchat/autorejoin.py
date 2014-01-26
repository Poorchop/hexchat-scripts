import hexchat

__module_name__ = 'AutoRejoin'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('Autorejoin script loaded')

def autorejoin_callback(word, word_eol, user_data):
	context = hexchat.get_context()
	hexchat.hook_timer(3000, rejoin_timer_callback, { 'context': context, 'channel': context.get_info('channel') })

def rejoin_timer_callback(user_data):
	user_data['context'].command('join {0}'.format(user_data['channel']))

hexchat.hook_print('You Kicked', autorejoin_callback)

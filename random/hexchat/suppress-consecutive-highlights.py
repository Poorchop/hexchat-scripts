import hexchat
import collections
import datetime

__module_name__ = 'Suppress-Consecutive-Highlights'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('Suppress-Consecutive-Highlights loaded')

LastHighlightRecord = collections.namedtuple('LastHighlightRecord', ['nickname', 'time'])

last_highlights = {}

def highlight_callback(word, word_eol, user_data):
	if hexchat.get_info('channel') == '(Highlights)':
		return hexchat.EAT_NONE
	
	word = [(word[i] if len(word) > i else '') for i in range(4)]
	
	result = hexchat.EAT_NONE
	
	now = datetime.datetime.now()
	dictionary_key = '{0}{1}'.format(hexchat.get_info('network'), hexchat.get_info('channel'))
	
	last_highlight = last_highlights.get(dictionary_key)
	
	if last_highlight is not None and last_highlight.nickname == word[0] and (now - last_highlight.time).total_seconds() <= 5 * 60:
		hexchat.emit_print(user_data, word[0], word[1], word[2], word[3])
		result = hexchat.EAT_HEXCHAT
	
	last_highlights[dictionary_key] = LastHighlightRecord(word[0], now)
	
	return result

def reset_last_highlight_callback(word, word_eol, user_data):
	dictionary_key = '{0}{1}'.format(hexchat.get_info('network'), hexchat.get_info('channel'))
	
	last_highlights[dictionary_key] = None

hexchat.hook_print('Channel Msg Hilight', highlight_callback, 'Channel Message')
hexchat.hook_print('Channel Action Hilight', highlight_callback, 'Channel Action')

hexchat.hook_print('Channel Message', reset_last_highlight_callback)
hexchat.hook_print('Channel Action', reset_last_highlight_callback)

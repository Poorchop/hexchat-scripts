import hexchat
import itertools
import re

__module_name__ = 'Rainbows'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('Rainbows script loaded')

colors = itertools.cycle((
	('05', '10'),
	('04', '12'),
	('07', '02'),
	('08', '06'),
	('09', '13'),
	('03', '15'),
	('11', '14'),
	('10', '05'),
	('12', '04'),
	('02', '07'),
	('06', '08'),
	('13', '09'),
	('15', '03'),
	('14', '11'),
))

fab_hook = None
in_fab_hook = False

color_code_regex = re.compile(r'(?:(?:{0}\d\d?(?:,\d\d?)?))'.format('\003'))
color_code_or_regular_character_regex = re.compile(r'((?:{0}\d\d?(?:,\d\d?)?)|.)'.format('\003'))

def fab_callback(word, word_eol, user_data):
	global in_fab_hook
	
	in_fab_hook = True
	hexchat.command(
		'say {0}'.format(
			' '.join(
				''.join(
					add_color(c) for c in color_code_or_regular_character_regex.split(w) if c
				) for w in word_eol[1].split(' ')
			)
		)
	)
	in_fab_hook = False
	
	return hexchat.EAT_ALL

def fab2_callback(word, word_eol, user_data):
	global in_fab_hook
	
	in_fab_hook = True
	hexchat.command(
		'say {0}'.format(
			''.join(
				add_color_and_background_color(c) for c in color_code_or_regular_character_regex.split(word_eol[1]) if c
			)
		)
	)
	in_fab_hook = False
	
	return hexchat.EAT_ALL

def spoiler_callback(word, word_eol, user_data):
	hexchat.command(
		'say {0}'.format(
			''.join(
				add_spoiler_color(c) for c in color_code_or_regular_character_regex.split(word_eol[1]) if c
			)
		)
	)
	
	return hexchat.EAT_ALL

def add_color(character):
	if color_code_regex.match(character):
		return character
	else:
		next_color, _ = next(colors)
		return '\003{0}{1}'.format(next_color, character)

def add_color_and_background_color(character):
	if color_code_regex.match(character):
		return character
	else:
		next_color, next_bg_color = next(colors)
		return '\003{0},{1}{2}'.format(next_color, next_bg_color, character)

def add_spoiler_color(character):
	if color_code_regex.match(character):
		return character
	else:
		next_color, _ = next(colors)
		return '\003{0},{0}{1}'.format(next_color, character)

def enfab_callback(word, word_eol, user_data):
	global fab_hook
	
	if fab_hook is None:
		fab_hook = hexchat.hook_command('', fab_passthru_callback)
		hexchat.prnt('Fabulous mode on')
	
	return hexchat.EAT_ALL

def defab_callback(word, word_eol, user_data):
	global fab_hook
	
	if fab_hook is not None:
		hexchat.unhook(fab_hook)
		fab_hook = None
		hexchat.prnt('Fabulous mode off')
	
	return hexchat.EAT_ALL

def fab_passthru_callback(word, word_eol, user_data):
	global in_fab_hook
	
	if in_fab_hook:
		return hexchat.EAT_NONE
	else:
		hexchat.command('fab {0}'.format(word_eol[0]))
		
		return hexchat.EAT_ALL

hexchat.hook_command('fab', fab_callback)
hexchat.hook_command('fab2', fab2_callback)
hexchat.hook_command('spoiler', spoiler_callback)
hexchat.hook_command('enfab', enfab_callback)
hexchat.hook_command('defab', defab_callback)

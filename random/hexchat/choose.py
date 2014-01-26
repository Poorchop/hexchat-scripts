import hexchat
import random
import re

__module_name__ = 'Choose'
__module_version__ = '1.0'
__module_description__ = ''

hexchat.prnt('Choose script loaded')

channels = frozenset(('#arnavion', '#vodka-subs', '#noko', '#sage',))
other_bots = frozenset(('Belfiore',))

choose_regex = re.compile(r'\.(?:(?:c(?:hoose)?)|(?:erande)|(?:選んで)|(?:選ぶがよい)) (.+)$')
order_regex = re.compile(r'[.!]o(?:rder)? (.+)$')
decimal_range_regex = re.compile(r'(-?\d+(\.\d+)?)-(-?\d+(\.\d+)?)$')
int_range_regex = re.compile(r'(-?\d+)-(-?\d+)$')

def choose_callback(word, word_eol, user_data):
	channel = hexchat.get_info('channel')
	
	if (channel in channels) and not (set(user.nick for user in hexchat.get_list('users')) & other_bots):
		option = None
		user = None
		input = None
		
		matches = choose_regex.match(word[1])
		if matches:
			option = 'CHOOSE'
			user = word[0]
			input = matches.group(1)
		else:
			matches = order_regex.match(word[1])
			if matches:
				option = 'ORDER'
				user = word[0]
				input = matches.group(1)
		
		if option == 'CHOOSE' or option == 'ORDER':
			for action in (try_choose, try_order):
				response = action(option, input)
				if response != None:
					context = hexchat.get_context()
					hexchat.hook_timer(0, send_response, { 'context': hexchat.get_context(), 'user': user, 'response': response })
					break
	
	return hexchat.EAT_NONE

def try_choose(option, input):
	if option != 'CHOOSE':
		return None
	
	matches = decimal_range_regex.match(input)
	
	if matches:
		matches = [matches.group(i) for i in range(1, 5)]
		matches[0] = float(matches[0])
		matches[2] = float(matches[2])
		
		if matches[1] or matches[3]:
			response = random.uniform(matches[0], matches[2])
		else:
			matches[0], matches[2] = sorted((matches[0], matches[2]))
			response = random.randint(matches[0], matches[2])
	
	else:
		choices = [choice for choice in (choice.strip() for choice in input.split(',')) if choice]
		if choices:
			if len(choices) == 1:
				choices = [choice for choice in (choice.strip() for choice in choices[0].split(' ')) if choice]
			
			response = random.choice(choices)
	
	return response

def try_order(option, input):
	if option != 'ORDER':
		return None
	
	matches = int_range_regex.match(input)
	if matches:
		matches = sorted(int(matches.group(i)) for i in range(1, 3))
		
		matches[1] = min(matches[1], matches[0] + 9)
		
		choices = [str(choice) for choice in range(matches[0], matches[1] + 1)]
		random.shuffle(choices)
		response = ', '.join(choices)
	
	else:
		choices = [choice for choice in (choice.strip() for choice in input.split(',')) if choice]
		if choices:
			if len(choices) == 1:
				choices = [choice for choice in (choice.strip() for choice in choices[0].split(' ')) if choice]
			
			random.shuffle(choices)
			response = ', '.join(choices)
	
	return response

def send_response(user_data):
	user_data['context'].command("say {0}: {1}".format(user_data['user'], user_data['response']))
	return None

hexchat.hook_print('Channel Message', choose_callback, 'Channel Message')
hexchat.hook_print('Channel Msg Hilight', choose_callback, 'Channel Msg Hilight')
hexchat.hook_print('Your Message', choose_callback, 'Your Message')

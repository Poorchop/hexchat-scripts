import datetime
import hexchat

__module_name__ = "Ignore DCC Spam"
__module_author__ = "PDog"
__module_version__ = "0.0.1"
__module_description__ = "Automatically detect DCC spammers and add them to ignore"

dcc_senders = {}

def dcc_spam_cb(word, word_eol, userdata):
	sender = word[0] + "_" + word[1]
	
	if sender + "_one" in dcc_senders: # <nickname>_<filename>_one
		dcc_senders[sender + "_two"] = datetime.datetime.now()
		time_one = dcc_senders[sender + "_one"]
		time_two = dcc_senders[sender + "_two"]
		
		if time_two + datetime.timedelta(seconds=-5) <= time_one:
			hexchat.command("IGNORE {0}".format(word[0]))
			hexchat.prnt("-\00322\002DCC-spam\002\00399-\t\002{0}\002 has been added to ignore".format(word[0]))
			del dcc_senders[sender + "_one"]
			del dcc_senders[sender + "_two"]
		else:
			dcc_senders[sender + "_one"] = time_two
			del dcc_senders[sender + "_two"]
	
	else:
		dcc_senders[sender + "_one"] = datetime.datetime.now()
	
	return hexchat.EAT_NONE

hexchat.hook_print("DCC SEND Offer", dcc_spam_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")
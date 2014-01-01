import hexchat
import re

__module_name__ = "AdFilter"
__module_author__ = "PDog"
__module_version__ = "0.1.1"
__module_description__ = "Move fserve advertisements to a separate tab"

# Add channels from which you would like to filter ads, e.g. channels = ["#freenode", "#defocus", "##linux"]
channels = ["#ebooks"]

# Customize the name of the tab to your liking
tab_name = "(Ads)"

omenserve_regex = re.compile(".*?Type:\s+\W[\w-]+\s+For\sMy\sList\sOf:\s+[\d,]+\s+Files\s+.*?Slots:\s+\d+/\d+\s+.*?Queued:\s+\d+\s+.*?Speed:\s+[\d,]+cps\s+.*?Next:\s+\w+\s+.*?Served:\s+[\d,]+\s+.*?List:\s+[A-Z][a-z]+\s+\w+\s+.*?Search:\s+[A-Z]{2,3}\s+.*?Mode:\s+\w+\s+.*?$")
bwi_regex = re.compile("^(\[BWI\])\sType\s+\W[\w-]+\s+to\sget\sthe\slist\sof\s+[\d,]+\s+files\s\([\d\.]+\s+[A-Z]+\)\.\s+Updated\son\s+[\d+-]+\s+[\d:]+\s+Total\sSent\(channel\):\s+[\d,]+\s+\([\d\.]+\s+[A-Z]+(\))$")

ad_lst = [omenserve_regex, bwi_regex]

def find_adtab():
	context = hexchat.find_context(channel=tab_name)
	if context == None:
		hexchat.command("NEWSERVER -noconnect {0}".format(tab_name))
		return hexchat.find_context(channel=tab_name)
	else:
		return context
		
def adfilter_cb(word, word_eol, userdata):

	word = [(word[i] if len(word) > i else "") for i in range(4)]

	global channels
	global ad_lst
	channel = hexchat.get_info("channel")
	stripped_msg = hexchat.strip(word[1], -1, 3)
	
	for ad in ad_lst:
		if ad.match(stripped_msg) and channel in channels:
			ad_context = find_adtab()
			ad_context.prnt("{0}\t\00318<{4}{3}{1}>\00399 {2}".format(channel, *word))
			return hexchat.EAT_ALL
			
def unload_cb(userdata):
	for chan in hexchat.get_list("channels"):
		if chan.type == 1 and chan.channel == tab_name:
			ad_context = hexchat.find_context(channel=tab_name)
			ad_context.command("CLOSE")
	hexchat.prnt(__module_name__ + " version " + __module_version__ + " unloaded")

hexchat.hook_print("Channel Message", adfilter_cb)
hexchat.hook_unload(unload_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")
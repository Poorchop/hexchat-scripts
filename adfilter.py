import hexchat
import re

__module_name__ = "AdFilter"
__module_author__ = "PDog"
__module_version__ = "0.3"
__module_description__ = "Move fserve advertisements to a separate tab"

# Add channels from which you would like to filter ads, e.g. channels = ["#freenode", "#defocus", "##linux"]
channels = []

# Customize the name of the tab to your liking
tab_name = "(Ads)"

bwi_regex          = re.compile("^(\[BWI\])\sType\s+\W[\w-]+\s+to\sget\sthe\slist\sof\s+[\d,]+\s+files\s\([\d\.]+\s+[A-Z]+\)\.\s+Updated\son\s+[\d+-]+\s+[\d:]+\.?\s+Total\sSent\(channel\):\s+[\d,]+\s+\([\d\.]+\s+[A-Z]+(\))$")
irssi_fserve_regex = re.compile("^(\(FServe Online\))\s+Note:\(Type\s+\W[\w-]+\s+for\s+filelist\)\s+Trigger:\(/ctcp\s+.*?\)\s+On\s+FServe:\(.*?\)\s+Sends:\(")
iterati_regex      = re.compile(".*?Type\s+\W[\w-]+\s+to\sget\smy\slist(\s|\.)?.*?\s+(Upd|(C|c)re)ated\son\s+[SMTWF][a-z]{2}\s+[A-Z][a-z]+\s+[\d\s:]+(\.).*?")
ns_fserve_regex    = re.compile("^(Type)\s+\W.*?for\smy\stiny\slist.*?[\d,]+\s+book(s)?\sadded\son\s+[\d\.]+\s+:\s+[\w\W]+")
omenserve_regex    = re.compile(".*?Type:\s+\W[\w-]+\s+For\sMy\sList\sOf:\s+[\d,]+\s+Files\s+.*?Slots:\s+\d+/\d+\s+.*?Queued:\s+\d+\s+.*?Speed:\s+[\d,]+cps\s+.*?Next:\s+\w+\s+.*?Served:\s+[\d,]+\s+.*?List:\s+[A-Z][a-z]+\s+\w+\s+.*?Search:\s+[A-Z]{2,3}\s+.*?Mode:\s+\w+\s+.*?$")
os_limits_regex    = re.compile("^(\s+)?(Sent:)\s+.*?To:\s+.*?Total\s+Sent:\s+[\d,]+\s+Files.*?Yesterday:\s[\d,]+\s+Files.*?Today.*?:\s+[\d,]+\s+Files.*?OS-Limits\s+(v[\d\.]+)$")
single_file_regex  = re.compile("^(\s+)?Type:\s+\W[\w-]+.*?To\sGet\sThis\s+.*?(File|MP3)$")
unknown_one_regex  = re.compile("^(Type)\s+\W[\w-]+\s+for\smy\slist\sof\s+\([\d,]+\)\s+Ebooks\screated\son\s+[\d-]+\s+([\d:]+)$")

ad_lst = [bwi_regex, irssi_fserve_regex, iterati_regex, ns_fserve_regex, omenserve_regex, os_limits_regex, single_file_regex, unknown_one_regex]
server_nicks = []

moved = False

def find_adtab():
	context = hexchat.find_context(channel=tab_name)
	if context == None:
		hexchat.command("NEWSERVER -noconnect {0}".format(tab_name))
		return hexchat.find_context(channel=tab_name)
	else:
		return context
		
def adfilter_cb(word, word_eol, userdata):

	word = [(word[i] if len(word) > i else "") for i in range(4)]

	global server_nicks
	channel = hexchat.get_info("channel")
	stripped_msg = hexchat.strip(word[1], -1, 3)
	
	for ad in ad_lst:
		if ad.match(stripped_msg) and channel in channels:
		
			if word[0] not in server_nicks:
				server_nicks.append(word[0])
				
			ad_context = find_adtab()
			ad_context.prnt("{0}\t\00318<{4}{3}{1}>\00399 {2}".format(channel, *word))
			return hexchat.EAT_ALL

def ctcpfilter_cb(word, word_eol, userdata):
	global moved
	
	if moved:
		return
	
	if (word[0][:5] == "SLOTS" or word[1] in server_nicks) and word[2] in channels:
		ad_context = find_adtab()
		
		moved = True
		ad_context.emit_print("CTCP Generic to Channel", *word)
		moved = False
		
		return hexchat.EAT_ALL

def unload_cb(userdata):
	for chan in hexchat.get_list("channels"):
		if chan.type == 1 and chan.channel == tab_name:
			ad_context = hexchat.find_context(channel=tab_name)
			ad_context.command("CLOSE")
	hexchat.prnt(__module_name__ + " version " + __module_version__ + " unloaded")

hexchat.hook_print("Channel Message", adfilter_cb)
hexchat.hook_print("CTCP Generic to Channel", ctcpfilter_cb)
hexchat.hook_unload(unload_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")
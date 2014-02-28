import re
import hexchat

__module_name__ = "RequestFilter"
__module_author__ = "PDog"
__module_version__ = "0.3"
__module_description__ = "Move search and file requests to a separate tab"

# Add channels from which you would like to filter requests, e.g. channels = ["#freenode", "#defocus", "##linux"]
channels = []

# Customize the name of the tab to your liking
tab_name = "(Requests)"

request_regex = re.compile("^![\w\\\[\]{}^`|-]+.*?\.([\w\d]{3,4}(\s+)?)$")
search_regex = re.compile("^@[\w\\\[\]{}^`|-]+")

def find_requesttab():
    context = hexchat.find_context(channel=tab_name)
    if context == None:
        hexchat.command("NEWSERVER -noconnect {0}".format(tab_name))
        return hexchat.find_context(channel=tab_name)
    else:
        return context

def requestfilter_cb(word, word_eol, userdata):
    word = [(word[i] if len(word) > i else "") for i in range(4)]

    channel = hexchat.get_info("channel")
	
    if channel in channels:
        if request_regex.match(word[1]) or search_regex.match(word[1]):
            request_context = find_requesttab()
            request_context.prnt("{0}\t\00318<{4}{3}{1}>\00399 {2}".format(channel, *word))

            return hexchat.EAT_ALL
		
def unload_cb(userdata):
    for chan in hexchat.get_list("channels"):
        if chan.type == 1 and chan.channel == tab_name:
            ad_context = hexchat.find_context(channel=tab_name)
            ad_context.command("CLOSE")
    hexchat.prnt(__module_name__ + " version " + __module_version__ + " unloaded")
	
hexchat.hook_print("Channel Message", requestfilter_cb, priority=hexchat.PRI_HIGH)
hexchat.hook_unload(unload_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

import re
import hexchat

__module_name__ = "RequestFilter"
__module_author__ = "PDog"
__module_version__ = "0.2"
__module_description__ = "Move search and file requests to a separate tab"

# Add channels from which you would like to filter requests, e.g. channels = ["#freenode", "#defocus", "##linux"]
channels = ["#ebooks", "#bookz"]

# Customize the name of the tab to your liking
tab_name = "(Requests)"

request_regex = re.compile("^![\w\\\[\]{}^`|-]+.*?\.([\w\d]{3,4}(\s+)?)$")
search_words = ["@find", "@new", "@search", "@seek"]
search_nicks = []

def build_search_nicks():
        global search_nicks

        for user in hexchat.get_list("users"):
                if "@" + user.nick not in search_nicks:
                        search_nicks.append("@" + user.nick)

def find_requesttab():
        context = hexchat.find_context(channel=tab_name)
        if context == None:
                hexchat.command("NEWSERVER -noconnect {0}".format(tab_name))
                return hexchat.find_context(channel=tab_name)
        else:
                return context

def requestfilter_cb(word, word_eol, userdata):
        word = [(word[i] if len(word) > i else "") for i in range(4)]

        split_words = word[1].split(" ")
        channel = hexchat.get_info("channel")
	
        if channel in channels:	
                build_search_nicks()
	
                if request_regex.match(word[1]) or split_words[0].lower() in search_words or split_words[0].split("-")[0] in search_nicks:
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

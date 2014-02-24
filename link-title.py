from urllib2 import Request, urlopen, HTTPError
import glob
import mimetypes
import os
import re
import hexchat

__module_name__ = "Link Title"
__module_author__ = "PDog"
__module_version__ = "0.2"
__module_description__ = "Display website title when a link is posted in chat"

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    hexchat.prnt("\002Link Title\002: Please install python-BeautifulSoup")
    hexchat.command("TIMER 0.1 PY UNLOAD {0}".format(__module_name__))

# TODO: Add support for threading, handle encoding properly, and test with Python 3 <PDog>

events = ("Channel Message", "Channel Action",
          "Channel Msg Hilight", "Channel Action Hilight")

def find_yt_script():
    script_path = os.path.join(hexchat.get_info("configdir"),
                          "addons", "get-youtube-video-info.py")

    if glob.glob(script_path):
        return re.compile("https?://(?!(w{3}\.)?youtu\.?be(\.|/))")
    else:
        return re.compile("https?://")

def mimetype(url):
    mimetype = mimetypes.guess_type(url)

    if mimetype[0]:
        split_type = mimetype[0].split("/")
        return split_type[0]
    else:
        return mimetype[0]

def get_title(url):
    mtype = mimetype(url)
    
    if mtype == "text" or not mtype:
        req = Request(url)

        try:
            response = urlopen(req)
            html_doc = response.read().decode("utf-8", "ignore")
            response.close()
            soup = BeautifulSoup(html_doc)
            msg = u"\0033\002::\003 Title\002 " + \
                  u"\0033\002::\003\002 {0}".format(soup.title.string)
            msg = msg.encode("utf-8")
            hexchat.prnt(msg)
        except HTTPError as e:
            msg = "\0033\002::\003 Title\002 " + \
                  "\0033\002::\003\002 {0}: {1}".format(str(e.code), e.reason)
            hexchat.prnt(msg)

def event_cb(word, word_eol, userdata):
    for w in word:
        stripped_word = hexchat.strip(w, -1, 3)
        
        if find_yt_script().match(stripped_word):
            url = stripped_word
            get_title(url)

    return hexchat.EAT_NONE
            

for event in events:
    hexchat.hook_print(event, event_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

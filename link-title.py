from urllib2 import Request, urlopen, HTTPError
import glob
import mimetypes
import re
import sys
import hexchat
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    hexchat.prnt("\002Link Title\002: Please install python-BeautifulSoup")

__module_name__ = "Link Title"
__module_author__ = "PDog"
__module_version__ = "0.1"
__module_description__ = "Display website title when a link is posted in chat"

# TODO: Add support for threading and test with Python 3 <PDog>

events = ["Channel Message", "Channel Action",
          "Channel Msg Hilight", "Channel Action Hilight"]

def find_yt_script():
    if sys.platform == "win32":
        script = "\addons\get-youtube-video-info.py"
    else:
        script = "/addons/get-youtube-video-info.py"

    path = hexchat.get_info("configdir") + script

    if glob.glob(path):
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
    if mimetype(url) == "text" or not mimetype(url):
        req = Request(url)

        try:
            response = urlopen(req)
            html_doc = response.read().decode("utf-8")
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

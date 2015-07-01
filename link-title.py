from html.parser import HTMLParser
import glob
import os
import re
import requests
import threading
import hexchat
import urllib3
requests.packages.urllib3.disable_warnings()

__module_name__ = "Link Title"
__module_author__ = "PDog"
__module_version__ = "0.6"
__module_description__ = "Display website title when a link is posted in chat"

# TODO: Merge py2/py3 branches <PDog>

events = ("Channel Message", "Channel Action",
          "Channel Msg Hilight", "Channel Action Hilight",
          "Private Message", "Private Message to Dialog",
          "Private Action", "Private Action to Dialog")

def find_yt_script():
    script_path = os.path.join(hexchat.get_info("configdir"),
                               "addons", "get-youtube-video-info.py")

    if glob.glob(script_path):
        return re.compile("https?://(?!(w{3}\.)?youtu\.?be(\.|/))")
    else:
        return re.compile("https?://")

def snarfer(html_doc):
    try:
        snarf = html_doc[html_doc.index("<title>")+7:html_doc.index("</title>")][:431]
    except ValueError:
        snarf = ""
    return snarf

def print_title(url, chan, nick, mode, cont):
    try:
        r = requests.get(url, verify=False)
        if r.headers["content-type"].split("/")[0] == "text":
            html_doc = r.text
            r.close()
            title = snarfer(html_doc)
            title = HTMLParser().unescape(title)
            title = title.lstrip()
            msg = u"\0033\002::\003 Title:\002 {0} " + \
                  u"\0033\002::\003 URL:\002 \00318\037{1}\017 " + \
                  u"\0033\002::\003 Posted by:\002 {3}{2} " + \
                  u"\0033\002::\002"
            msg = msg.format(title, url, nick, mode)
            # Weird context and timing issues with threading, hence:
            cont.command("TIMER 0.1 DOAT {0} ECHO {1}".format(chan, msg))
    except requests.exceptions.RequestException as e:
        print(e)

def event_cb(word, word_eol, userdata, attr):
    # ignore znc playback
    if attr.time:
        return
    
    word = [(word[i] if len(word) > i else "") for i in range(4)]
    cur_context = hexchat.get_context()
    chan = cur_context.get_info("channel")
    
    for w in word[1].split():
        stripped_word = hexchat.strip(w, -1, 3)
        
        if find_yt_script().match(stripped_word):
            url = stripped_word

            if url.endswith(","):
                url = url[:-1]
                
            threading.Thread(target=print_title, args=(url, chan, word[0], word[2], cur_context)).start()

    return hexchat.EAT_NONE
            

for event in events:
    hexchat.hook_print_attrs(event, event_cb)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

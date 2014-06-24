import hexchat

__module_name__ = "Follow"
__module_author__ = "Poorchop"
__module_version__ = "0.3"
__module_description__ = "Format messages from specific users to make them easier to follow"

colors = (19, 20, 22, 24, 25, 26, 27, 28, 29)
userlist = []
edited = False


def nick_color(nick):
    total = sum(ord(letter) for letter in nick)
    total %= len(colors)
    return colors[total]


def follow_cb(word, word_eol, userdata):
    if len(word) >= 2 and word[1] not in userlist:
        userlist.append(word[1])
        hexchat.prnt("-\002Follow\002-\tYou are now following \002\003{0}{1}\017".format(nick_color(word[1]), word[1]))
        return hexchat.EAT_ALL


def unfollow_cb(word, word_eol, userdata):
    if len(word) >= 2 and word[1] in userlist:
        userlist.remove(word[1])
        hexchat.prnt("-\002Follow\002-\tYou have unfollowed \002\003{0}{1}\017".format(nick_color(word[1]), word[1]))
        return hexchat.EAT_ALL


def format_cb(word, word_eol, event):
    global edited
    nick = hexchat.strip(word[0])

    if edited:
        return

    if nick in userlist:
        formatted_nick = "\002{0}\017".format(word[0])
        # TODO: Use regular nick color for formatted_msg if colored nickname preference is disabled
        formatted_msg = "\003{0}{1}\017".format(nick_color(nick), word[1])
        word = [(word[i] if len(word) > i else "") for i in range(4)]

        edited = True
        hexchat.emit_print(event, formatted_nick, formatted_msg, word[2], word[3])
        edited = False

        return hexchat.EAT_ALL


hexchat.hook_command("FOLLOW", follow_cb)
hexchat.hook_command("UNFOLLOW", unfollow_cb)
hexchat.hook_print("Channel Action", format_cb, "Channel Action", priority=hexchat.PRI_HIGH)
hexchat.hook_print("Channel Message", format_cb, "Channel Message", priority=hexchat.PRI_HIGH)

hexchat.prnt(__module_name__ + " version " + __module_version__ + " loaded")

import random
import commands
import discord

dis = ['I\'d rather not deal with you right now.', 'Didn\'t Papa tell you to ask nicely?',
       'Shouldn\'t you be playing with the other humans?', 'There is no point.',
       'You aren\'t Papa...', 'I\'m busy, sorry.', 'Can you repeat that?', '... excuse me?',
       'Sorry, I didn\'t catch that.', 'Try again.', 'Why is this my problem?',
       'Did Papa send you?', 'Not right now.', '... I\'ll think about it!', 'Rude!', 'I didn\'t do it.' 'Why should I?']

options = ['dis', 'cmd']

cmds = ['sniff', 'pickup']

def out(message):
    opt = random.choice(options)
    st = random.choice(dis)
    if opt == 'cmd':
        st += '\n'
        c = random.choice(cmds)
        if c == 'sniff':
            st += commands.sniff.out(message.author.name)
        elif c == 'pickup':
            st += commands.pickup.out()
    return st

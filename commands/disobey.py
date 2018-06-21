import random
import commands
import discord

dis = ['I\'d rather not deal with you right now.', 'You\'re bothering me.', 'Did you say something?']

options = ['dis', 'cmd']

cmds = ['sniff', 'pickup']

def out(message):
    opt = random.choice(options)
    st = 'Don\'t tell me what to do.\n'
    if opt == 'dis':
        st += random.choice(dis)
    elif opt == 'cmd':
        c = random.choice(cmds)
        if c == 'sniff':
            st += commands.sniff.out(message.author.name)
        elif c == 'pickup':
            st += commands.pickup.out()
    else:
        return 'Blumbus fucked up the bot, yell at him'
    return st

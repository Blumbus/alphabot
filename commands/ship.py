import random
import discord

def out(thing1, thing2):
    name1 = thing1
    name2 = thing2
    disp1 = thing1
    disp2 = thing2
    if type(thing1) is discord.User or type(thing1) is discord.Member:
        name1 = thing1.id
        disp1 = thing1.display_name
    if type(thing2) is discord.User or type(thing2) is discord.Member:
        name2 = thing2.id
        disp2 = thing2.display_name
    random.seed = bin(name1) + bin(name2)
    val = round(random.random())
    return '**' + str(disp1) + '** and **' + str(disp2) + '**... a ' + str(val) + '% ship rate!'

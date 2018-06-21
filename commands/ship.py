import random
import discord

def out(thing1, thing2):
    name1 = thing1
    name2 = thing2
    disp1 = thing1
    disp2 = thing2
    if isinstance(thing1, discord.User):
        print('thing1!')
        name1 = thing1.id
        disp1 = thing1.display_name
    if isinstance(thing2, discord.User):
        print('thing2!')
        name2 = thing2.id
        disp2 = thing2.display_name
    random.seed = bin(name1) + bin(name2)
    val = round(random.random())
    return '**' + str(disp1) + '** and **' + str(disp2) + '**... a ' + str(val) + '% ship rate!'

import random
import discord

def out(thing1, thing2):
    name1 = thing1
    name2 = thing2
    disp1 = thing1
    disp2 = thing2
    if isinstance(thing1, discord.User):
        name1 = thing1.id
        disp1 = thing1.display_name
    if isinstance(thing2, discord.User):
        name2 = thing2.id
        disp2 = thing2.display_name
    v = sum(ord(x) for x in name1) + sum(ord(x) for x in name2)
    random.seed = v
    r = random.random() * 100
    print(r)
    val = round(r)
    return '**' + str(disp1) + '** and **' + str(disp2) + '**... a ' + str(val) + '% ship rate!'

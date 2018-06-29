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
    random.seed(v)
    r = (random.random() + random.random()) * 50
    print(r)
    val = round(r)
    ret = '**' + str(disp1) + '** and **' + str(disp2) + '**... a ' + str(val) + '% ship rate!\n'
    if val > 95:
        ret += 'These two are perfect, absolutely perfect!'
    elif val > 80:
        ret += random.choice(['An inseparable pair! Papa would be proud.', '(whistles)'])
    elif val > 60:
        ret += random.choice(['Impressive... these two make a great duo.', 'My my, these two are something special.'])
    elif val > 40:
        ret += random.choice(['Could be better.', 'The synergy could use some work.', 'More effort into it might help.'])
    elif val > 20:
        ret += random.choice(['Low... as expected of humans.', 'Hardly a spark.'])
    else:
        ret += random.choice(['There\'s no connection here at all... disgusting.', 'You\'d have better results paired with a rock.'])
    return ret

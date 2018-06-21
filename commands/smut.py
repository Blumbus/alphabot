import discord
import random

combos = ['icecream', 'handjob', 'deep']

def out(server, user=False):
    cmb = random.choice(combos)
    return combo(cmb, server, user)


males = ['Hiro', 'Futoshi', 'Mitsuru', 'Alpha', 'Goro', 'Zorome']
females = ['Zero Two', 'Kokoro', 'Ichigo', 'Ikuno', 'Miku']
def person(server, user=False):
    if user:
        return get_user(server)
    ppl = males + females
    return random.choice(ppl)

def male(server, user=False):
    if user:
        return get_user(server)
    return random.choice(males)

def female(server, user=False):
    if user:
        return get_user(server)
    return random.choice(females)


def get_user(server):
    m = random.choice(list(server.members))
    return m.name


adjs = ['gentle', 'furious', 'loving', 'slow']
def adjective():
    return random.choice(adjs)


def combo(cmb, server, user=False):
    if cmb == 'icecream':
        return 'Ice cream smeared between ' + person(server, user) + ' and ' + person(server, user) + '\'s lips'
    elif cmb == 'handjob':
        return person(user) + ' giving ' + male(server, user) + ' a ' + adjective() + ' handjob'
    elif cmb == 'deep':
        return person(server, user) + ' attempting to fit all ' + str(random.randint(5, 9)) + ' inches of ' + male(server, user) + ' inside their mouth '
    else:
        return 'Blumbus fucked up the bot, yell at him'
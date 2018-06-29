import random

grs = ['Welcome, %USER%, watch your step', 'Hey there, %USER%', 'Nice to see yoy, %USER%', '%USER%, do I know you?', 'Ah, welcome home, %USER%',
'Did you take a shower today, %USER%?', 'Did you bring your pride, %USER%?']

def out(id):
    g = random.choice(grs)
    g = g.replace('%USER%', '<@' + id + '>')
    return g
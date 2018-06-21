import random

grs = ['Welcome, %USER%', 'Hey there, %USER%', 'Henlo %USER%', '%USER% isn\'t who you think they are. But they\'re here now.', 'Look who it is! %USER% from... you-know-where.',
'Did you take a shower today, %USER%?', 'I don\'t remember seeing you before, %USER%. You must be new.']

def out(id):
    g = random.choice(grs)
    g = g.replace('%USER%', '<@' + id + '>')
    return g
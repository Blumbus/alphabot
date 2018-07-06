import random

grs = ['Welcome, %USER%, watch your step', 'Hey there, %USER%', 'Nice to see you, %USER%',
       '%USER%, do I know you?', 'Ah, welcome home, %USER%', 'Smells like %USER% got here safe and sound',
       'I have never smelled anything like you before, %USER&', 'This smell... %USER%... it\'s the scent of a loser',
'Did you take a shower today, %USER%?', 'Did you bring your pride, %USER%?']


def out(id):
    g = random.choice(grs)
    g = g.replace('%USER%', '<@' + id + '>')
    return g
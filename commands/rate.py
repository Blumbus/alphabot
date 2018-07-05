import random
import discord

def out(words):
    user = False
    if len(words) == 1 and isinstance(words[0], discord.User):
        user = True
    st = ''
    for w in words:
        conc = w
        if isinstance(w, discord.User):
            conc = str(w.id)
        st += conc
    v = sum(ord(x) for x in st)
    random.seed(v)
    r = random.random() * 10
    print(r)
    val = round(r)
    if random.random() < 0.1:
        val += 1
    ret = ''
    aan = 'a'
    if val == 8 or val == 11:
        aan = 'an'
    punc = '...'
    if val > 10:
        punc = '!!'
    elif val > 7:
        punc = '!'
    elif val > 3:
        punc = '.'
    if user:
        ret = '**' + words[0].display_name + '**... I give them ' + aan + ' ' + str(val) + '/10' + punc
    else:
        ret = 'I give it ' + aan + '... ' + str(val) + '/10' + punc
    if 'ass' in st or 'butt' in st:
        if val > 9:
            ret += '\nPerfect! Round! Huge!'
        elif val > 5:
            ret += '\nPlump as a peach!'
        elif val > 2:
            ret += '\nI\'d still take it.'
        else:
            ret += '\nFlat...'
    return ret

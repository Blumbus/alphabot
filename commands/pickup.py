import random
import datetime

lines = ['What was it Iota called him? Is that what you want me to be?', 'So I\'m your-- darling, was it?',
         'I\'m flattered, I suppose.', 'No thanks.', 'Thanks, but no thanks.', 'No chance.',
         'Try again later.', 'Disgusting.', 'Absolutely disgusting.', 'I know what you\'re thinking.',
         'Papa wouldn\'t approve.', 'No.', 'There are plenty of others to choose from.',
         'Do you want to ride with me?', '(licks lips)', '(kisses your hand)',
         'I like it when you\'re forward.', 'Honesty is attractive.',
         'I\'m flattered, but no.', 'That\'s cute.', 'The answer is still no.', '(shrugs)',
         'I\'d like that-- don\'t get the wrong idea.', 'Please, don\'t.', 'I\'ve already told you no.',
         'Stop asking.', 'Ugh.', 'This again?', 'Why do you want me?', 'Uh, no.', '(squints)',
         '(tilts head)', 'Why?', '(stares)', '(blinks)', '(tilts head)']


def out(words):
    st = ''
    for w in words:
        st += w
    v = sum(ord(x) for x in st)
    random.seed(v + int(datetime.datetime.now().strftime("%Y%m%d")))
    st = random.choice(lines)
    return st

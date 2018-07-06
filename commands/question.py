import random

maybe = ['You already know the answer.', 'I\'d love to answer, but that\'s confidential.',
           'That\'s best discovered through introspection.', 'I\'m flattered, but I\'m not omnipresent.',
           'Yes and no.', 'What do you think?', 'Would you prefer a *yes* or *no*?', 'I decline to answer.',
           'Hmmm...', 'Hm? What was that?', 'Were you speaking to me?', 'Who knows.',
           'I\'m not certain.', 'I\'m not interested in this conversation.', 'I have better things to do, you know.',
           'You don\'t have anyone else to talk to, do you?',
           'It\'s fine to admit you don\'t have anything else to do.']

conf = ['Yes.', 'No.', 'Perhaps...', 'You wish.', 'If only.', 'Of course.', 'I suppose.', 'Yes?', 'No?',
        'Nah.', 'Yeah.', 'Maybe.', 'I don\'t know.', '(nodding)', '(shakes head)', 'Nope.', 'Yep.']

def out():
    ret = ''
    if random.random() < 0.75:
        ret = random.choice(conf)
    else:
        ret = random.choice(maybe)
    return ret
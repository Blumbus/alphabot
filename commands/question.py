import random

maybe = ['Don\'t you know this already?', '(laughs)', '(snickers)', 'You know this one.', 'Oh, please.',
         'What do you think?', 'Ehhhh...', 'Hmmm...', 'Hm? What was that?', 'Who knows.', '(blinks and shrugs)',
         'I\'m not sure, honestly.', 'I\'m a bit too busy for this conversation.', 'Really?',
         'You don\'t have anyone else to talk to, do you?',
         'It\'s fine to admit you don\'t have anything else to do.', 'That\'s up to you!']

conf = ['Yes.', 'No.', 'Perhaps...', 'You wish.', 'If only.', 'Of course.', 'I suppose.', 'Yes?', 'No?',
        'Nah.', 'Yeah.', 'Maybe.', 'I don\'t know.', '(nodding)', '(shakes head)', 'Nope.', 'Yep.']

def out():
    ret = ''
    if random.random() < 0.75:
        ret = random.choice(conf)
    else:
        ret = random.choice(maybe)
    return ret
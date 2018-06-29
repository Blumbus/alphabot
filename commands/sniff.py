import random

smells = ['Smells like trash.', 'What a wonderful scent!', 'Good enough.', 'A bit spicy.', 'A bit dry.', 'A bit sour.', 'A tad bitter.', 'Too sweet.',
          'Salty.', 'Like body odor.', 'Unappealing.', 'Smells a bit... nutty.', 'Toasted too long.',
          'Burnt flesh? Hmm...', 'Familiar.', 'I caught a whiff of chocolate.', 'Too vanilla for me.',
          'Smells like disappointment.', '(sneezes)', 'Smoking is bad for you.',
          'Are you old enough to drink?', 'Do I smell watermelon?', '... Whatever I smell, it\'s bad.',
          'Did you forget your deodorant?', 'That\'s some cheap cologne.', 'Smells like a secret.',
          'You should take a shower.', 'You smell... *nice*.', 'That\'s a human alright.',
          'Humans smell interesting.', 'I\'ve smelled worse... I guess.', 'Cheese, eh?',
          'You have a lot of potential.', 'Smells like jealousy.', 'Smells like lust.', 'Smells like greed.',
          'Let me get a... *closer* sniff.']

def out(username):
    random.seed(abs(hash(username)))
    return '**' + str(username) + '**... ' + random.choice(smells)
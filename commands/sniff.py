import random

smells = ['Smells like trash.', 'What a wonderful scent!', 'Good enough.', 'A bit spicy.', 'A bit dry.', 'A bit sour.', 'A tad bitter.', 'Too sweet.',
          'Salty.', 'Like body odor.', 'Unappealing.', 'Smells a bit... nutty.', 'Toasted too long.',
          'Burnt flesh? Hmm...', 'Familiar.', 'I caught a whiff of chocolate.', 'Too vanilla for me.',
          'Smells like disappointment.', '(sneezes)', 'I suppose I\'ll just have to pick my nose until I can smell something else.']

def out(username):
    random.seed(abs(hash(username)))
    return '**' + str(username) + '**... ' + random.choice(smells)
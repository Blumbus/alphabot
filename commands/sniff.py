import random
import discord
import datetime

smells = ['Smells like cheese.', 'Smoking is bad for you.', 'Are you old enough to drink?', 'Do I smell watermelon?',
          '... Whatever I smell, it\'s bad.', 'Did you put on deodorant yet?', 'You\'re wearing cheap cologne.',
          '(sneezes)', '(coughs)', 'Ugh...', '(leans away immediately)', 'Smells like a secret.',
          'You should take a shower.', 'Heh... you smell nice.', 'That\'s a human, alright.',
          'Humans smell interesting.', 'I\'ve smelled worse, I guess.', '(sniffs more)', '(sniffs closer)',
          '(sniffs from a different angle)', 'Chocolate, eh?', 'You have a lot of potential.',
          'Hey, come back.', 'Smells like jealousy.', 'Smells good.', 'This is... the scent of a loser...',
          'You missed your morning coffee.', 'Stress doesn\'t smell good.', 'Oooh... sweet.', 'That\'s spicy.',
          'Fruity! Like you!', 'Brush your teeth!', 'Floral perfume!', 'Ah, sour attitude.',
          'Dry, like your humor.', 'Been drinking again, I see.', 'You must be a good cook... or know one.',
          'Better head to a laundromat.', 'I want some of that... no, not like that! What you ate!']

def out(user):
    print('datetime: ' + str(int(datetime.datetime.now().strftime("%Y%m%d"))))
    print('idk: ' + str(sum(ord(x) for x in user.id)))
    random.seed(int(sum(ord(x) for x in user.id))) + int(datetime.datetime.now().strftime("%Y%m%d"))
    return '**' + str(user.display_name) + '**... ' + random.choice(smells)
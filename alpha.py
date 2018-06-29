import discord
from commands import *
from settings import *
import random

TOKEN = 'NDMzODQwMTU1MjU5MDQzODUw.DbBs2g.3dtafJ1z0y8eEsp3cgnu80Ebau8'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    serv = message.server.id
    chan = message.channel.id
    if serv not in config.servers:
        return

    usrs = message.mentions
    primary = message.author
    message.content = message.content.lower().strip()
    if len(usrs) > 0:
        primary = usrs[0]
    words = []
    words = message.content.split()
    if message.content.startswith(config.command_prefix):
        message.content = message.content[1:].strip()
        words[0] = words[0][1:]
        for user in message.mentions:
            for i in range(0, len(words)):
                if words[i] == '<@' + user.id + '>':
                    words[i] = user
        new_words = []
        bracc_start = -1
        curr_word = ''
        for i in range(0, len(words)):
            if isinstance(words[i], discord.User):
                new_words.append(words[i])
            elif words[i].startswith('[') and bracc_start == -1:
                if words[i].endswith(']'):
                    new_words.append(words[i][1:-1])
                else:
                    curr_word = words[i][1:]
                    bracc_start = i
            elif bracc_start != -1:
                if words[i].endswith(']'):
                    curr_word += ' ' + words[i][:-1]
                    bracc_start = -1
                    new_words.append(curr_word)
                else:
                    curr_word += ' ' + words[i]
            else:
                new_words.append(words[i])
        words = new_words

        if command_perms(message, words[0]):
            if random.random() < 0.08:
                await client.send_message(message.channel, disobey.out(message))
            else:
                if words[0] == 'pickup':
                    await client.send_message(message.channel, pickup.out())
                elif words[0] == 'smut':
                    user = '-user' in message.content
                    print(user)
                    await client.send_message(message.channel, smut.out(message.server, user))
                elif words[0] == 'sniff':
                    await client.send_message(message.channel, sniff.out(primary.name))
                elif words[0] == 'ship':
                    print('len: ' + str(len(words)))
                    if len(words) < 2:
                        await client.send_message(message.channel, 'Please specify at least one thing to ship.')
                    else:
                        if len(words) == 2:
                            print('1 arg')
                            thing1 = message.author
                            thing2 = words[1]
                        else:
                            print('2 args')
                            thing1 = words[1]
                            thing2 = words[2]
                        await client.send_message(message.channel, ship.out(thing1, thing2))
        else:
            print('permission denied in channel!')
    if command_perms(message, 'chat'):
        test_content = message.content = message.clean_content.lower().strip()
        print(test_content)
        if (test_content.startswith('is') or test_content.startswith('does') or test_content.startswith('am') or test_content.startswith('should') or test_content.startswith('are') or
                test_content.startswith('do') or test_content.startswith('was') or test_content.startswith('will') or test_content.startswith('were') or
                test_content.startswith('can') or test_content.startswith('did') or test_content.startswith('has') or test_content.startswith('could')) and test_content[len(message.content)-1] == '?':
            await client.send_message(message.channel, question.out())


def command_perms(msg, cmd):
    perm = cmd
    if perm not in config.servers[msg.server.id]['commands']:
        perm = 'default'
    if config.servers[msg.server.id]['commands'][perm] == 'all':
        return True
    if msg.channel.id in config.servers[msg.server.id]['commands'][perm]['white']:
        return True
    return False

@client.event
async def on_member_join(member):
    await client.send_message(member.server.get_channel(config.servers[member.server.id]['greet']), greet.out(member.id))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
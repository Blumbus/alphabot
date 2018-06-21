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
    if serv not in config.servers:
        return

    usrs = message.mentions
    primary = message.author
    message.content = message.clean_content.lower().strip()
    if len(usrs) > 0:
        primary = usrs[0]
    words = []
    words = message.content.split(' ', 1)
    if message.content.startswith(config.command_prefix):
        message.content = message.content[1:].strip()
        print(message.content)

        if random.random() < 0.08:
            await client.send_message(message.channel, disobey.out(message))
        else:
            if message.content.startswith('pickup'):
                await client.send_message(message.channel, pickup.out())
            elif message.content.startswith('smut'):
                user = '-user' in message.content
                print(user)
                await client.send_message(message.channel, smut.out(message.server, user))
            elif message.content.startswith('sniff'):
                await client.send_message(message.channel, sniff.out(primary.name))
    test_content = message.content = message.clean_content.lower().strip()
    print(test_content)
    if (test_content.startswith('is') or test_content.startswith('does') or test_content.startswith('am') or test_content.startswith('should') or test_content.startswith('are') or
            test_content.startswith('do') or test_content.startswith('was') or test_content.startswith('will') or test_content.startswith('were') or
            test_content.startswith('can') or test_content.startswith('did') or test_content.startswith('has') or test_content.startswith('could')) and test_content[len(message.content)-1] == '?':
        await client.send_message(message.channel, question.out())


@client.event
async def on_member_join(member):
    await client.send_message(member.server.get_channel(config.servers[member.server.id]['main']), greet.out(member.id))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
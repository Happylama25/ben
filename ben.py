import disnake, random, os
from dotenv import load_dotenv
from disnake.ext import commands
load_dotenv('.env')
token = os.getenv('TOKEN')
choices = [1, 2, 3, 4]

client = disnake.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ben'):
        choice = random.choice(choices)
        if choice == 1:
            await message.channel.send('yes <:benYES:966139457784938556>')
        elif choice == 2:
            await message.channel.send('no <:benNO:966139600730980382>')
        elif choice == 3:
            await message.channel.send('hahaha! <:hahaha:966142354337705984>')
        else:
            await message.channel.send('ugh... <:ugh:966143370634358894>')

client.run(token)

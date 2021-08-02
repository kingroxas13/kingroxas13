import discord
import os
 
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
   return

  if message.content.startswith('Cat'):
    await message.channel.send('Sensational!')
  
@client.event
async def on_message(message):
  if message.content.startswith('Alex'):
    await message.channel.send('Cool!')

my_secret = os.environ['TOKEN']
client.run(my_secret)
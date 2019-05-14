import requests 
import discord
import json

#Connect to website and pull json for specified event
url = "https://imehi.me/participants/"
data = {'event':9} 
response = requests.post(url = url, data = data)
json = json.loads(response.text)

pingList = []
for entry in json:
    pingList.append(entry["userid"])

#get bot token
file = f=open("res/token.txt", "r")
token = file.read()


client = discord.Client()

@client.event
async def on_ready():
    guild = await client.fetch_guild(532437793805303808)
    channels = guild.text_channels
    for channel in channels:
        if channel.id == 534093319089946629:
            channel.send('hello')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!yeet'):
        await message.channel.send('Yeet')
    
    if message.content.startswith('!test'):
        guild = await client.fetch_guild(532437793805303808)
        for id in pingList:
            user = await guild.fetch_member(id)
            await message.channel.send(user.mention)

        
client.run(token.strip())



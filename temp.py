import requests 
import discord
import json
import sys

event = sys.argv[1]

#Connect to website and pull json for specified event
url = "https://imehi.me/participants/"
data = {'event':event} 
response = requests.post(url = url, data = data)
json = json.loads(response.text)

pingList = []
for entry in json:
    pingList.append(entry["userid"])

#get bot token
file = f=open("res/token.txt", "r")
token = file.read()

#get channel to send message to
file = f=open("res/channel.txt", "r")
channelid = file.read()
channelid = int(channelid.strip())


client = discord.Client()

@client.event
async def on_ready():
    guild = await client.fetch_guild(532437793805303808)
    channels = client.get_all_channels()

    #go through all channels the bot has access to, find specified channel
    for channel in channels:
        if channel.id == channelid:
            message = ""
            for id in pingList:
                user = await guild.fetch_member(id)
                message += user.mention + " "
            await channel.send(message)
            await sys.exit()
        
client.run(token.strip())



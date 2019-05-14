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


client = discord.Client()

@client.event
async def on_ready():
    print('I have connected')
    guild = await client.fetch_guild(532437793805303808)
    channels = client.get_all_channels()
    for channel in channels:
        if channel.id == 577895915319459862:
            message = ""
            for id in pingList:
                user = await guild.fetch_member(id)
                message += user.mention + " "
            await channel.send(message)
            sys.exit()
        
client.run(token.strip())



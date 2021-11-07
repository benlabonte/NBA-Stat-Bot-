import discord
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
Token=os.getenv('discord_token')


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!p'):
        input_string= message.content[2:].title().strip()

        response=requests.get('https://peaceful-hamlet-39904.herokuapp.com/player/{player}'.format(player = input_string))
        response_json=json.loads(response.text)
        player_name = response_json['player_name']
        timeframe= response_json['timeframe']
        pts= response_json['pts']
        ast= response_json['ast']
        reb= response_json['reb']
        jersey= response_json['jersey']
        team_name= response_json['team_name']

        await message.channel.send('{player}\n{team}\n'.format(player=player_name, team=team_name))
client.run(Token)
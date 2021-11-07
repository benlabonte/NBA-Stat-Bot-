import discord
import os
from discord import player
from dotenv import load_dotenv
import requests
import json

load_dotenv()
Token=os.getenv('discord_token')

client=discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!p'):
        input_string= message.content[2:].title().strip()
        response=requests.get('https://peaceful-hamlet-39904.herokuapp.com/player/{player}'.format(player = input_string))
        response_json=json.loads(response.text)
        player_namepy = response_json['player_name']
        timeframepy= response_json['timeframe']
        ptspy= response_json['pts']
        astpy= response_json['ast']
        rebpy= response_json['reb']
        jerseypy= response_json['jersey']
        team_namepy= response_json['team_name']
        player_split=input_string.lower().split()
        player_unscore=player_split[0] + '_' + player_split[1]

        embed=discord.Embed(
        title=player_namepy,
        url="https://ca.global.nba.com/players/#!/{player_url}".format(player_url=player_unscore),
        description=team_namepy,
        color=discord.Color.blue())
    await message.channel.send(embed=embed)

client.run(Token)



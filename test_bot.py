import discord
import os
from discord import player
from dotenv import load_dotenv
import requests
import json
from colors import colors

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
        if input_string.lower() == 'lebron james':
            response=requests.get('https://peaceful-hamlet-39904.herokuapp.com/player/LeBron James')
        elif input_string.lower()=='demar derozan':
            response=requests.get('https://peaceful-hamlet-39904.herokuapp.com/player/DeMar DeRozan')
        elif input_string.lower()== 'lamarcus aldridge':
            response=requests.get('https://peaceful-hamlet-39904.herokuapp.com/player/LaMarcus Aldridge')
        elif input_string.lower()== 'fred vanvleet':
            response=requests.get('https://peaceful-hamlet-39904.herokuapp.com/player/Fred VanVleet')
        elif input_string.lower()=='lamelo ball':
            response=requests.get('https://peaceful-hamlet-39904.herokuapp.com/player/LaMelo Ball')
        else:
            response=requests.get('https://peaceful-hamlet-39904.herokuapp.com/player/{player}'.format(player = input_string))
        if (response.text == "Error - No player by that name was found.") :
            embed_data=discord.Embed(
                title='Error',
                description="No player by that name was found. Please check your spelling.",
                color=colors.Bulls)
            await message.channel.send(embed=embed_data)
            return
        response_json=json.loads(response.text)
        player_idpy = response_json['player_id']
        player_namepy = response_json['player_name']
        timeframepy= response_json['timeframe']
        ptspy= response_json['pts']
        astpy= response_json['ast']
        rebpy= response_json['reb']
        jerseypy= response_json['jersey']
        team_namepy= response_json['team_name']
        player_split=input_string.lower().split()
        player_unscore=player_split[0] + '_' + player_split[1]
        team_colour_lookup = team_namepy
        if team_colour_lookup == "76ers":
            team_colour_lookup = "Philly"
        elif team_colour_lookup == "Trail Blazers":
            team_colour_lookup = "TrailBlazers"

        embed_data=discord.Embed(
        title='{player_name} (#{jersey})'.format(player_name=player_namepy, jersey=jerseypy),
        url="https://ca.global.nba.com/players/#!/{player_url}".format(player_url=player_unscore),
        description=team_namepy,
        color=getattr(colors, team_colour_lookup))

        embed_data.set_thumbnail(url='https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{id}.png'.format(id=player_idpy))
        embed_data.add_field(name='**Seasonal Average Statline** ({timeframe})'.format(timeframe=timeframepy), value='Pts: {0:.1f} - Reb: {1:.1f} - Ast: {2:.1f}'.format(ptspy, rebpy, astpy), inline=False)
        await message.channel.send(embed=embed_data)

client.run(Token)



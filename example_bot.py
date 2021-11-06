import discord

discord_token = "OTA2NjA1MTQ2MjI4ODE4MDQw.YYbD1g.GLYyAGP7ghrRccUNACPB7FhvOhk"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(discord_token)
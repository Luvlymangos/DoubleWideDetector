import discord
from discord.utils import *
from discord.ext import commands
import asyncio
import os
import random

currentworkingdirectory = os.getcwd()
authtoken = None
Reaction = None
Daemon = 915401001186521118
intents = discord.Intents.all()
with open(currentworkingdirectory+'/token.txt', 'r') as openfile:
    authtoken = openfile.readline()
    openfile.close()


client = commands.Bot(command_prefix= '!', intents=intents, case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'{client.user} has started and is in {len(client.guilds)} Guild(s)')

@client.event
async def on_member_join(member):
    if member.id == Daemon:
        try:
            await member.guild.system_channel.send(":clown: **WARNING DOUBLE WIDE CLOWN JOINING**:clown:")
        except:
            pass

@client.event
async def on_message(message):
    global Reaction
    if message.author != client.user:
        if message.author.id == Daemon:

            try:
                Reaction = await message.add_reaction("🤡")
            except Exception as e:
                if e.code == 90001:
                    await message.channel.send("**🤡 DOUBLE WIDE HAS BLOCKED THE BOT 🤡**")



    await client.process_commands(message)


async def main(): 
    await client.start(authtoken)
asyncio.run(main())

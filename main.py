import discord
import os
from discord.ext import commands
from ruamel.yaml import YAML

yaml = YAML()

with open("./config.yml", "r", encoding="utf-8") as file:
    config = yaml.load(file)

bot = commands.Bot(command_prefix=config["Prefix"], description='Bluff Bath Bot')


@bot.event
async def on_ready():
    print('Bot Ready')


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send('Welcome {0.mention}!'.format(member))


@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == config["Welcome-Message-ID"]:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if payload.emoji.name == '✅':
            role = discord.utils.get(guild.roles, name='Fresher')
            member = payload.member
            await member.add_roles(role)

for file in os.listdir('cogs'):
    if file.endswith('.py'):
        name = file[:-3]
        bot.load_extension(f'cogs.{name}')

bot.run(config["Token"])
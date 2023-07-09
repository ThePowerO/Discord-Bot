import discord
from discord.ext import commands
import os
import aiohttp
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def rules(ctx):
        await ctx.reply(f"1- Do not spam messages{os.linesep}2- Look at announciaments")

@bot.command()
async def updatedate(ctx):
    image_url = "https://cdn.discordapp.com/attachments/777317677470580756/1119556806767820830/fetchimage.png"

    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as resp:
            if resp.status == 200: 
                with open("image.png", "wb") as file:
                    file.write(await resp.read())
                file = discord.File("image.png")
                await ctx.reply(file=file)
            else:
                await ctx.send("An error occured while getting the image.")

@bot.command()
async def grandpiece(ctx):
     await ctx.reply(f"https://www.roblox.com/games/1730877806/SEASON-2-Grand-Piece-Online")

@bot.command()
async def bloxfruits(ctx):
     await ctx.reply(f"https://www.roblox.com/games/2753915549/Blox-Fruits")
        
@bot.command()
async def bedwars(ctx):
        await ctx.reply(f'https://www.roblox.com/games/6872265039/BedWars-SEASON-8')

@bot.command()
async def murdermystery2(ctx):
        await ctx.reply(f'https://www.roblox.com/games/142823291/Murder-Mystery-2')

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

@bot.command()
async def playersBF(ctx):
    url = "https://www.roblox.com/games/2753915549/Blox-Fruits"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, 'html.parser')
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Blox Fruits is: {players_count}")
            else:
                await ctx.reply("Unable to get number of players at the moment.")

@bot.command()
async def playersMM2(ctx):
    url = "https://www.roblox.com/games/142823291/Murder-Mystery-2"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, 'html.parser')
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                layers_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Murder Mystery 2 is: {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

@bot.command()
async def playersBW(ctx):
    url = "https://www.roblox.com/games/6872265039/BedWars-SEASON-8"
    async with aiohttp.ClientSession() as sesison:
        async with sesison.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, 'html.parser')
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Bed Wars is {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

bot.run("Token")

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
        await ctx.reply(f"1- Do not spam messages{os.linesep}2- Look at announciaments.")

@bot.command()
async def updatedate(ctx):
    image_url = "https://cdn.discordapp.com/attachments/777317677470580756/1119556806767820830/fetchimage.png"

    async with aiohttp.ClientSession() as session: # create a asynchronous sesion that allow to do asynchronous HTTP solicitation.
        async with session.get(image_url) as resp: # "resp" stores the response of the HTTP solicitation made by "session.get(image_url)".
            if resp.status == 200: # "200" is an HTTP status code that indicates a successful response.

                with open("image.png", "wb") as file: #"image.png" is name(can be whatever but let format of image) wb to open as binary recording
                    file.write(await resp.read())
                file = discord.File("image.png")
                await ctx.reply(file=file) #the variable file turns to "file"(whatever name)
            else:
                await ctx.send("An error occured while getting the image.")

@bot.command()
async def grandpiece(ctx):
     await ctx.reply(f"https://www.roblox.com/games/1730877806/SEASON-2-Grand-Piece-Online")

@bot.command()
async def bloxfruits(ctx):
     await ctx.reply(f"https://www.roblox.com/games/2753915549/Blox-Fruits")

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
    async with aiohttp.ClientSession() as session: #ClientSession represents a HTTP session and provides methods to send HTTP solicitations
        async with session.get(url) as resp:
            #use session to start a HTTP GET solicitation to the url (get() method returns an asynchronous ClientResponse object, which contains the HTTP response.)
            if resp.status == 200: #if good status or response of the website
                html = await resp.text() #text() extract the content to resp (content of the HTTP)
                soup = BeautifulSoup(html, 'html.parser')
                #BfSp analyze the HTML content (the one we want to), html parser is an internal implamentation of BfSp to analyze the HTML content
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                #soup's find method (finds the first <p> element that has class attributed equals to "acording to the HTML class name")
                #The find() method returns the first element that matches the search criteria.
                players_count = players_element.text.strip() #we access the "players_element" text using .text, .strip() to remove extra whitespace
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
                await ctx.reply(f"The current number of players playing Bed Wars is: {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

@bot.command()
async def playersAF2(ctx):
    url = "https://www.roblox.com/games/6299805723/Update-37-x5-Anime-Fighters-Simulator"
    async with aiohttp.ClientSession() as sesison:
        async with sesison.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, 'html.parser')
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Anime Fighters 2 is {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

@bot.command()
async def playersArsenal(ctx):
    url = "https://www.roblox.com/games/286090429/Arsenal"
    async with aiohttp.ClientSession() as sesison:
        async with sesison.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                soup = BeautifulSoup(html, 'html.parser')
                players_element = soup.find('p', {'class': 'text-lead font-caption-body wait-for-i18n-format-render'})
                players_count = players_element.text.strip()
                await ctx.reply(f"The current number of players playing Arsenal is {players_count}")
            else:
                await ctx.reply("Unable to get the number of players at the moment.")

@bot.command()
async def playersTSB(ctx):
    url = "https://www.roblox.com/games/10449761463/The-Strongest-Battlegrounds"

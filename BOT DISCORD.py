import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = "INSERT BOT PREFIX")

@client.event
async def on_ready():
    print("BOT IS READY")

@client.event
async def on_message(message):
    if message.content == "MESSAGE NUMBER ONE":
        await client.send_message(message.channel, "ANSWER MESSAGE NUMBER ONE")
    if message.content == "MESSAGE NUMBER 2":
        await client.send_message(message.channel, "ANSWER MESSAGE NUMBER 2")
    if message.content == "SAY HELLO TO THE PERSON":
        await client.send_message(message.channel, "HELLO @NICKNAME")
    if message.content == "TEXT NUMBER 3":
        await client.send_message(message.channel, "ANSWER NUMBER 3")
    if message.content == "TXT NUMBER 4":
        await client.send_message(message.channel, "ANSW TXT 4")
    if message.content.upper().startswith("HELLO BOT"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> HELLO PERSON" % (userID))
    if message.content.upper().startswith("!DI"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content == "TXT MESSAGE 5":
        await client.send_message(message.channel, "ANSW MESSAGE 5")
    if message.content == "TXT MESSAGE 6":
        await client.send_message(message.channel, "ANSW MESSAGE 6")
    if message.content == "TXT MESSAGE 7":
        await client.send_message(message.channel, "ANSW MESSAGE 7")
client.run("ENTER TOKEN DISCORD APP")

import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Client ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('---------Skedaddle---------')


@client.event
async def on_message(message):
    if message.content.startswith("?test"):
        channel = message.channel
        await channel.send("Estou vivo!")


client.run('TOKEN')

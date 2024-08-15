import discord
TOKEN = "MTI3MzQ4MzIyNDExNDQwMTMwMQ.GlEgtH.hkgLUL-sMQ8FxUf5aUoccxp7w3s7RMdWprkxhE"
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is connected to the following server:\n')
    for server in client.guilds:
        print(f'{server.name}(id: {server.id})')
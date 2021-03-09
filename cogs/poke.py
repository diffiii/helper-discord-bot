import asyncio
import discord
from discord.ext import commands


class Poke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def poke(self, ctx, member: discord.Member):
        await ctx.message.delete()
        current = member.voice.channel.id
        temp = 814840808296546314 if current == 770704857656328202 else 770704857656328202
        for i in range(3):
            await member.move_to(self.client.get_channel(temp))
            await asyncio.sleep(0.5)
            await member.move_to(self.client.get_channel(current))
            await asyncio.sleep(0.5)


def setup(client):
    client.add_cog(Poke(client))

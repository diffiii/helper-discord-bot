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
        if member.id == 593767655584956426: return
        current = member.voice.channel.id
        temp = 814840808296546314 if current == 770704857656328202 else 770704857656328202
        for i in range(3):
            try:
                await member.move_to(self.client.get_channel(temp))
            except:
                pass

            await asyncio.sleep(0.5)

            try:
                await member.move_to(self.client.get_channel(current))
            except:
                pass
            
            await asyncio.sleep(0.5)


def setup(client):
    client.add_cog(Poke(client))

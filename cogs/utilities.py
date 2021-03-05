import discord
from discord.ext import commands


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['ank'])
    @commands.has_permissions(manage_messages = True)
    async def ankieta(self, ctx, *, contents):
        await ctx.message.delete()

        message = await ctx.send(embed = discord.Embed(title = '**ANKIETA**', description = contents, color = 0xE8DB7D))
        await message.add_reaction('⬆️')
        await message.add_reaction('⬇️')

    @commands.command(aliases=['głosowanie', 'głos'])
    @commands.has_permissions(manage_messages = True)
    async def glosowanie(self, ctx, *, contents):
        await ctx.message.delete()

        message = await ctx.send(embed = discord.Embed(title = '**GŁOSOWANIE**', description = contents, color = 0x82204A))
        await message.add_reaction('⬆️')
        await message.add_reaction('⬇️')


def setup(client):
    client.add_cog(Utilities(client))

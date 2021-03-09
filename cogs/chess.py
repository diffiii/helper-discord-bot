import discord
from discord.ext import commands


class Chess(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['wyzwij'])
    async def wyzwanie(self, ctx, member: discord.Member, *, link):
        await ctx.message.delete()
        await member.send(embed = discord.Embed(title = f'{ctx.author} wyzywa cię do partii szachów!', description = link, color=0x00FFFF))


def setup(client):
    client.add_cog(Chess(client))

import discord
from discord.ext import commands
from main import load_json, write_json


class Nicks(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        nicks = load_json('nicks.json')

        for nick in nicks:
            if after.id == int(nick) and after.name != nicks[nick]:
                await after.edit(nick = nicks[nick])

    @commands.command(aliases = ['blok'])
    @commands.has_permissions(manage_nicknames = True)
    async def zablokuj(self, ctx, member: discord.Member, *, nick: str):
        await ctx.message.delete()

        nicks = load_json('nicks.json')
        if str(member.id) in nicks:
            del nicks[str(member.id)]
        nicks[member.id] = nick

        write_json('nicks.json', nicks)

    @commands.command(aliases = ['odblok'])
    @commands.has_permissions(manage_nicknames = True)
    async def odblokuj(self, ctx, member: discord.Member):
        await ctx.message.delete()

        nicks = load_json('nicks.json')
        del nicks[str(member.id)]

        write_json('nicks.json', nicks)


def setup(client):
    client.add_cog(Nicks(client))

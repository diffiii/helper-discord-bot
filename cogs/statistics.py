import re
import discord
from discord.ext import commands
from main import load_json, write_json


class Statistics(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def topka(self, ctx):
        stats = load_json('stats.json')
        stats = sorted(stats.items(), key=lambda item: item[1])[::-1][:10]
        final = []
        for i in range(10):
            final.append(f'{discord.utils.get(ctx.guild.emojis, name = stats[i][0])}: {stats[i][1]}')
        final = '\n'.join(final)
        await ctx.send(final)

    @commands.command()
    async def antytopka(self, ctx):
        stats = load_json('stats.json')
        stats = sorted(stats.items(), key=lambda item: item[1])[:10]
        final = []
        for i in range(10):
            final.append(f'{discord.utils.get(ctx.guild.emojis, name = stats[i][0])}: {stats[i][1]}')
        final = '\n'.join(final)
        await ctx.send(final)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != self.client.user.id:
            custom_emojis = re.findall(r'<:\w*:\d*>', message.content)
            custom_emojis = [int(e.split(':')[2].replace('>', '')) for e in custom_emojis]
            custom_emojis = [discord.utils.get(await message.guild.fetch_emojis(), id = e) for e in custom_emojis]
            stats = load_json('stats.json')
            for emoji in custom_emojis:
                stats[emoji.name] += 1
            write_json('stats.json', stats)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id != self.client.user.id:
            stats = load_json('stats.json')
            stats[reaction.emoji.name] += 1
            write_json('stats.json', stats)


def setup(client):
    client.add_cog(Statistics(client))

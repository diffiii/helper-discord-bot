import re
import discord
from discord.ext import commands
from main import load_json, write_json


class Statistics(commands.Cog):
    def __init__(self, client):
        self.client = client

    # @commands.command()
    # async def test(self, ctx):
    #     emojis = await ctx.guild.fetch_emojis()
    #     stats = {}
    #     for emoji in emojis:
    #         if emoji.animated == False:
    #             stats[emoji.name] = 0
    #     write_json('stats.json', stats)

    @commands.Cog.listener()
    async def on_message(self, message):
        custom_emojis = re.findall(r'<:\w*:\d*>', message.content)
        custom_emojis = [int(e.split(':')[2].replace('>', '')) for e in custom_emojis]
        custom_emojis = [discord.utils.get(await message.guild.fetch_emojis(), id = e) for e in custom_emojis]
        stats = load_json('stats.json')
        for emoji in custom_emojis:
            stats[emoji.name] += 1
        write_json('stats.json', stats)


def setup(client):
    client.add_cog(Statistics(client))

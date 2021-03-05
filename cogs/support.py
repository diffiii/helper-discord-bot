import discord
from discord.ext import commands


class Support(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['propo'])
    async def propozycja(self, ctx, *, contents):
        await ctx.message.delete()

        if ctx.message.channel.id in [770743052494176316, 776460154236305411]:
            message = await ctx.send(embed = discord.Embed(title = f'**PROPOZYCJA │ {ctx.author}**', description = contents, color = 0x66CCFF))
            emojis = ['👍' ,'👎', discord.utils.get(message.guild.emojis, name = 'POGGERS')]
            for emoji in emojis:
                await message.add_reaction(emoji)
        else:
            channel = discord.utils.get(ctx.guild.text_channels, name = '🔧│support')
            await ctx.send(f'Ten kanał nie służy do zgłaszania propozycji. Zrób to na kanale {channel.mention}.', delete_after = 15)

    @commands.command()
    async def problem(self, ctx, *, contents):
        await ctx.message.delete()

        if ctx.message.channel.id in [770743052494176316, 776460154236305411]:
            channel = discord.utils.get(ctx.guild.text_channels, name = '💼│administracja')
            message = await channel.send(embed = discord.Embed(title = f'**PROBLEM │ {ctx.author}**', description = contents, color = 0xFF0000))
        else:
            channel = discord.utils.get(ctx.guild.text_channels, name = '🔧│support')
            await ctx.send(f'Ten kanał nie służy do zgłaszania problemów. Zrób to na kanale {channel.mention}.', delete_after = 15)


def setup(client):
    client.add_cog(Support(client))

import discord
from discord.ext import commands
from datetime import datetime


class MessageEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.author.bot: return
        log_channel = await self.client.fetch_channel(774241128454029353)
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')
        contents = f'**Before:** {before.content}\n**After:** {after.content}'
        embed = discord.Embed(title = f'Message edited in #{after.channel.name}', description = contents, color = 0xFF9933) #FF9933
        embed.set_author(name = after.author, icon_url = after.author.avatar_url)
        embed.set_footer(text = f'ID: {after.author.id} • {timestamp}')
        await log_channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        log_channel = await self.client.fetch_channel(774241128454029353)
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')
        embed = discord.Embed(title = f'Message deleted in #{message.channel.name}', description = message.content, color = 0xFF3333) #FF3333
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.set_footer(text = f'ID: {message.author.id} • {timestamp}')
        await log_channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        log_channel = await self.client.fetch_channel(774241128454029353)
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')
        msgs = '\n'.join([f'[{message.author}]: {message.content}' for message in messages])
        embed = discord.Embed(title = f'Messages purged in #{messages[0].channel.name}', description = msgs, color = 0xFF6699) #FF6699
        embed.set_footer(text = f'ID: {messages[0].author.id} • {timestamp}')
        await log_channel.send(embed = embed)


def setup(client):
    client.add_cog(MessageEvents(client))

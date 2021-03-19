###############################
#     Helper 3.0 by diffi     #
###############################

import json
import discord
from discord.ext import commands
from random import choice

intents = discord.Intents.all()


def load_json(filename):
    """
    Load json contents from file.
    """
    with open(filename) as infile:
        return json.load(infile)

def write_json(filename, contents):
    """
    Write json contents to file.
    """
    with open(filename, 'w') as outfile:
        json.dump(contents, outfile, indent=4)


settings = load_json('settings.json')


class Helper(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = settings['prefix'], help_command = None, intents = intents)

        for extension in settings['extensions']:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'\nFailed to load extension "{extension}":\n> {type(e).__name__}: {e}')

    async def on_ready(self):
        await self.change_presence(activity = discord.Game(name = 'Gambit Sandomierski'))
        print(f'\nBot has been initialized.\n> Name: {self.user}\n> ID: {self.user.id}\n')

    async def on_message(self, message):
        if message.channel.id == 770743052494176316:
            if not message.content.startswith('.'):
                if message.author.id != self.user.id and message.author.id != 593767655584956426:
                    await message.delete()

        if message.content == '+1':
            if message.reference is not None:
                msg = await message.channel.fetch_message(message.reference.message_id)
                await msg.add_reaction(discord.utils.get(message.guild.emojis, name = 'plusJeden'))
                await message.delete()
            else:
                msg = await message.channel.history(limit = 2).flatten()
                await msg[1].add_reaction(discord.utils.get(message.guild.emojis, name = 'plusJeden'))
                await message.delete()

        if message.content == '-1':
            if message.reference is not None:
                msg = await message.channel.fetch_message(message.reference.message_id)
                await msg.add_reaction(discord.utils.get(message.guild.emojis, name = 'minusJeden'))
                await message.delete()
            else:
                msg = await message.channel.history(limit = 2).flatten()
                await msg[1].add_reaction(discord.utils.get(message.guild.emojis, name = 'minusJeden'))
                await message.delete()

        if self.user.mentioned_in(message):
            possibilities = [
                'czekaj bo gram w szachy teraz',
                'nie mogę teraz, zaszachował mnie ziomeczek',
                'daj mi chwilę, zaraz ci ten gambit sandomierski wytłumaczę',
                'a idź ty do kościoła',
                'moment, sprzątam plebanię'
            ]
            await message.channel.send(choice(possibilities))

        if message.author.bot: return

        for element in ['szachy', 'szaszki', 'piony', 'pionki']:
            if element in message.content.lower():
                await message.add_reaction(discord.utils.get(message.guild.emojis, name = 'gambit_sandomierski'))

        await self.process_commands(message)

    def run(self):
        super().run(settings['token'])


if __name__ == '__main__':
    client = Helper()
    client.run()

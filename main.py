###############################
#     Helper 3.0 by diffi     #
###############################

import json
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.members = True


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

        for element in ['szachy', 'szaszki', 'piony', 'pionki']:
            if element in message.content.lower():
                await message.add_reaction(discord.utils.get(message.guild.emojis, name = 'gambit_sandomierski'))

        await self.process_commands(message)

    def run(self):
        super().run(settings['token'])


if __name__ == '__main__':
    client = Helper()
    client.run()

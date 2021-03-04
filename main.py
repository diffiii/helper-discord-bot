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
        print(f'\nBot has been initialized.\n> Name: {self.user}\n> ID: {self.user.id}\n')

    def run(self):
        super().run(settings['token'])


if __name__ == '__main__':
    client = Helper()
    client.run()

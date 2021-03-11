import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount: int = 0):
        await ctx.message.delete()

        if 1 <= amount <= 100:
            await ctx.channel.purge(limit = amount)
        else:
            await ctx.send('Podana ilość wiadomości jest nieprawidłowa.', delete_after = 3)

    @commands.command(aliases = ['spr'])
    @commands.has_permissions(administrator = True)
    async def sprawdzian(self, ctx, date, time, subject, *, material):
        await ctx.message.delete()

        subjects = {
            "angwiencek": "Język angielski (Wiencek)",	
            "angurbaniec": "Język angielski (Urbaniec)",	
            "angwojcicka": "Język angielski (Wójcicka)",	
            "anguzup": "Język angielski uzupełniający",	
            "biol": "Biologia",	
            "chem": "Chemia",	
            "fiz": "Fizyka",	
            "geo": "Geografia",	
            "hist": "Historia",	
            "infzywczak": "Informatyka (Żywczak)",	
            "infherma": "Informatyka (Herma)",	
            "mat": "Matematyka",	
            "niemczader": "Język niemiecki (Czader)",	
            "niemsych": "Język niemiecki (Sych)",	
            "pol": "Język polski",	
            "pp": "Przedsiębiorczość",	
            "rel": "Religia",	
            "wos": "Wiedza o społeczeństwie"
        }

        title = f'{date} - {time} - {subjects[subject]}'
        description = f'{material}'

        await ctx.send(embed = discord.Embed(title = title, description = description, color = 0x00BBBB))


def setup(client):
    client.add_cog(Admin(client))

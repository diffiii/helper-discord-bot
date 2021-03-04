import re
import requests
import discord
from discord.ext import commands
from datetime import date


formval = lambda value: re.sub(r"(?<=.)(?=(?:...)+$)", ".", value)


class Covid19(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases = ('covid', 'cov'))
    @commands.has_permissions(administrator = True)
    async def covid19(self, ctx, tests: float = 0):
        await ctx.message.delete()

        today = date.today()
        data = requests.get('https://coronavirus-19-api.herokuapp.com/countries/Poland').json()

        if data:
            if data['todayCases'] != '0':
                factor      = int(round(data['todayCases'] / 383.5))
                cases       = formval(str(data['cases']))
                todayCases  = formval(str(data['todayCases'])), data['todayCases']
                todayTests  = f'{tests} tyś.' if tests != 0 else 'TBA'
                percentage  = f'{round(todayCases[1] / (tests * 1000) * 100, 2)}%' if tests != 0 else 'TBA'
                deaths      = formval(str(data['deaths']))
                todayDeaths = formval(str(data['todayDeaths']))
                recovered   = formval(str(data['recovered']))
                active      = formval(str(data['active']))
                critical    = formval(str(data['critical']))

                title = f'{today.day:02d}.{today.month:02d}.{today.year} - Stan na godzinę 10:30'
                description = f'LICZBA ZAKAŻEŃ NA 100.000 OSÓB: ~{factor}'
                embed = discord.Embed(title = title, description = description, color = 0xFF0000)
                embed.add_field(name = 'Liczba zakażeń (ogółem / dziś):', value = f'{cases} / {todayCases[0]}',   inline = True)
                embed.add_field(name = 'Liczba wykonanych testów:',       value = f'{todayTests} [{percentage}]', inline = True)
                embed.add_field(name = 'Liczba zgonów (ogółem / dziś):',  value = f'{deaths} / {todayDeaths}',    inline = True)
                embed.add_field(name = 'Liczba osób, które wyzdrowiały:', value = f'{recovered}',                 inline = True)
                embed.add_field(name = 'Liczba aktywnych zakażeń:',       value = f'{active}',                    inline = True)
                embed.add_field(name = 'Liczba przypadków krytycznych',   value = f'{critical}',                  inline = True)

                await ctx.send(embed = embed)
            else:
                await ctx.send('Dane aktualnie niedostępne.', delete_after=2)
        else:
            await ctx.send('Zapytanie nieudane.', delete_after=2)

    @commands.command(aliases = ('covidformat', 'format'))
    @commands.has_permissions(administrator = True)
    async def covid_format(self, ctx, date, factor, cases, todayCases, tests: float, deaths, todayDeaths, recovered, active, critical):
        await ctx.message.delete()

        todayTests  = f'{tests} tyś.'
        percentage = f'{round(int(todayCases) / (tests * 1000) * 100, 2)}%'
        
        title = f'{date} - Stan na godzinę 10:30'
        description = f'LICZBA ZAKAŻEŃ NA 100.000 OSÓB: ~{factor}'
        embed = discord.Embed(title = title, description = description, color = 0xFF0000)
        embed.add_field(name = 'Liczba zakażeń (ogółem / dziś):', value = f'{formval(cases)} / {formval(todayCases)}',   inline = True)
        embed.add_field(name = 'Liczba wykonanych testów:',       value = f'{todayTests} [{percentage}]',                inline = True)
        embed.add_field(name = 'Liczba zgonów (ogółem / dziś):',  value = f'{formval(deaths)} / {formval(todayDeaths)}', inline = True)
        embed.add_field(name = 'Liczba osób, które wyzdrowiały:', value = f'{formval(recovered)}',                       inline = True)
        embed.add_field(name = 'Liczba aktywnych zakażeń:',       value = f'{formval(active)}',                          inline = True)
        embed.add_field(name = 'Liczba przypadków krytycznych',   value = f'{formval(critical)}',                        inline = True)

        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Covid19(client))

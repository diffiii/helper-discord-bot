import discord
import numpy as np
from discord.ext import commands


class Game:
    def __init__(self, ctx):
        self.ctx = ctx
        self.turn = 'X'
        self.won = False
        self.board = np.full((3, 3), ' ')

    def c(self, x, y) -> str:
        return ':x:' if self.board[x][y] == 'X' else ':o:' if self.board[x][y] == 'O' else ':black_circle:'

    def get(self) -> str:
        return f'{self.c(0, 0)}{self.c(0, 1)}{self.c(0, 2)}\n{self.c(1, 0)}{self.c(1, 1)}{self.c(1, 2)}\n{self.c(2, 0)}{self.c(2, 1)}{self.c(2, 2)}'

    def change(self, index, turn) -> bool:
        if self.board[index] == ' ':
            self.board[index] = turn
            return True
        return False

    def check(self) -> bool:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or \
            self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ': return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
        self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ': return True
        return False

    def is_draw(self) -> bool:
        if self.board[0][0] != ' ' and self.board[0][1] != ' ' and self.board[0][2] != ' ' and \
           self.board[1][0] != ' ' and self.board[1][1] != ' ' and self.board[1][2] != ' ' and \
           self.board[2][0] != ' ' and self.board[2][1] != ' ' and self.board[2][2] != ' ' and not self.check():
            return True
        return False


class TicTacToe(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.game = None
        self.message = None

    async def end(self, ctx, info = None):
        await self.message.channel.send(info)
        await self.message.clear_reactions()
        self.game = None
        self.message = None

    @commands.command()
    async def ttt(self, ctx, member: discord.Member):
        await ctx.message.delete()
        if ctx.author.id == member.id and ctx.author.id != 593767655584956426:
            await ctx.send('Nie możesz zagrać sam ze sobą.', delete_after = 5)
            return
        emojis = ['↖️', '⬆️', '↗️', '⬅️', '⏺️', '➡️', '↙️', '⬇️', '↘️', '❌']
        if self.game is None:
            self.playerX = ctx.author
            self.playerO = member
            self.game = Game(ctx)
        else:
            await ctx.send('Aktualnie trwa inna gra.', delete_after=5)
            return
        self.message = await ctx.send(self.game.get())
        for emoji in emojis:
            await self.message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.id == self.message.id and user.id != self.client.user.id and self.game is not None:
            await self.message.remove_reaction(reaction, user)
            if reaction.emoji == '❌':
                await self.end(f'{user.mention} poddał grę!')
                return
            choices = {
                '↖️': (0, 0),
                '⬆️': (0, 1),
                '↗️': (0, 2),
                '⬅️': (1, 0),
                '⏺️': (1, 1),
                '➡️': (1, 2),
                '↙️': (2, 0),
                '⬇️': (2, 1),
                '↘️': (2, 2)
            }
            if (self.game.turn == 'X' and user.id == self.playerX.id) or (self.game.turn == 'O' and user.id == self.playerO.id):
                if self.game.change(choices[reaction.emoji], self.game.turn):
                    await self.message.edit(content = self.game.get())
                    if self.game.is_draw():
                        await self.end('Remis!')
                        return
                    if self.game.check():
                        winner = self.playerX.mention if self.game.turn == 'X' else self.playerO.mention
                        await self.end(f'{winner} wygrał(a)!')
                        return
                    else:
                        self.game.turn = 'O' if self.game.turn == 'X' else 'X'

    @commands.command()
    async def adminstop(self, ctx):
        self.game = None
        self.message = None


def setup(client):
    client.add_cog(TicTacToe(client))

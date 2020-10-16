from discord.ext import commands
from datetime import datetime as d
import os
from discord import File

class Request(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        name='request',
        description='Request Category to get all information recorded for that category ',
        aliases=['r']
    )  
    async def request(self, ctx):
        cat = str(ctx.message.content)
        cat = cat.split(' ',1)[1]
        path = "C:\\Users\\Simon\\Documents\\code\\PABOT\\Users\\"+str(ctx.message.author.id)
        if(cat == "sleep"):
            await ctx.send(file = File(path+'\\sleep.txt'),content='Here is your sleep data')
        if(cat == 'log'):
            await ctx.send(file = File(path+'\\log.txt'),content='Here are all recorded logs')

        return
def setup(bot):
    bot.add_cog(Request(bot))

from discord.ext import commands
from datetime import datetime as d
import os

class Log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        name='"',
        description='Records all messages that start with this command into a log ',
        aliases=['']
    )  
    async def record_message(self, ctx):
        time = d.timestamp(d.now())
        writepath = "C:\\Users\\Simon\\Documents\\code\\PABOT\\Users\\"+str(ctx.message.author.id)+"\\log.txt"
        mode = 'a' if os.path.exists(writepath) else 'w'
        with open(writepath,mode) as f:
            f.write("Message recored at :"+str(time)+'---' + str(ctx.message.content)+'\n')
        msg = await ctx.send(content='Message recored')
        return
def setup(bot):
    bot.add_cog(Log(bot))

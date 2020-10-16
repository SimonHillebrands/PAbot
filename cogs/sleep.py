from discord.ext import commands
import os
from datetime import datetime as d

class Sleep(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        name='gm',
        description='Records wake up time',
        aliases=['Good morning','morning','im up',"i'm up","i'm awake",'awake',"im awake",'up']
    )  
    async def wake_command(self, ctx):
        time = d.timestamp(d.now())
        writepath = "C:\\Users\\Simon\\Documents\\code\\PABOT\\Users\\"+str(ctx.message.author.id)+"\\sleep.txt"
        mode = 'a' if os.path.exists(writepath) else 'w'
        with open(writepath,mode) as f:
            f.write('w -'+str(time)+'\n')
        

        await ctx.send(content='Good Morning '+str(ctx.message.author))
        return
    @commands.command(
        name='gn',
        description='Records sleep time',
        aliases=['Good night','night','sleep','sleeping','night night']
    )      
    async def sleep_command(self,ctx):
        time = d.timestamp(d.now())
        writepath = "C:\\Users\\Simon\\Documents\\code\\PABOT\\Users\\"+str(ctx.message.author.id)+"\\sleep.txt"
        mode = 'a+' if os.path.exists(writepath) else 'w+'
        with open(writepath,mode) as f:
            f.write('s -'+str(time)+'\n')

        await ctx.send(content='Good Night '+str(ctx.message.author))
        return
def setup(bot):
    bot.add_cog(Sleep(bot))

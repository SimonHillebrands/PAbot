from discord.ext import commands
from datetime import datetime as d
import os
colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}
class Habit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        name='habit:',
        description='Used to set up a new habit/task ',
        aliases=['']
    )  
    async def habit(self, ctx):
        name = str(ctx.message.content)
        name = name.split(' ',1)[1]
        #not sure if this is neccesary, might try removing the check later
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author
        
        await ctx.send(content="Creating a habit named "+name+"how often would you like to do this habit?\n[1.daily,2.weekly,3.monthly]")
        msg = await self.bot.wait_for('message', check=check)
        #set to daily by default
        category = 1
        frequency = 1
        nxt_msg = "You have chosen the default options"
        nxt_nxt_msg = ""
        period = False
        if(msg.content == "0"):
            category = 1
        if(msg.content == "1" or msg.content.lower() == "daily"):
            category = 1
            await ctx.send(content="How many times per day?\n[1,2,3...]\nOr would you like to repeat every n days?[p1,p2,p3...]")
            msg = await self.bot.wait_for('message', check=check)
            if(msg.content[0] = "p"):
                period = True 
                msg.content = msg.content[1:]
            frequency = int(msg.content)
            if(frequency<7 and not(period)):
                await ctx.send(content="Would you like to specify which days of the week?\nSimply type each day followed by a space[MON,TUE,WEN,TH,FRI,SAT,SUN]")
                msg = await self.bot.wait_for('message', check=check)
        if(msg.content == "2" or msg.content.lower() == "weekly"):
            category = 2
            await ctx.send(content="How many times per week?\n[1,2,3...]\n Or would you like to repeat ever n weeks?[p1,p2,p3...]")
            msg = await self.bot.wait_for('message', check=check)
            if(msg.content[0] = "p"):
                period = True 
                msg.content = msg.content[1:]
            frequency = int(msg.content)           
        if(msg.content == "3" or msg.content.lower() == "monthly"):
            category = 3
            await ctx.send(content="How many times per month?\n[1,2,3...]\nOr would you like to repeat ever n months?[p1,p2,p3...]")
            msg = await self.bot.wait_for('message', check=check)
            if(msg.content[0] = "p"):
                period = True 
                msg.content = msg.content[1:]
            frequency = int(msg.content)  








        
        return
def setup(bot):
    bot.add_cog(Log(bot))

from discord.ext import commands
import time
from datetime import datetime
from time import mktime
import mysql.connector
from mysql.connector import Error
from db import *
from dateutil.parser import parse
from dateutil.tz import gettz
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
        habit_name = str(ctx.message.content)
        habit_name = habit_name.split(' ',1)[1]
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

        comp = [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "Click me!",
                        "style": 1,
                        "custom_id": "click_one"
                    }
                ]

            }
        ]
        await ctx.send(content="Creating a habit named "+habit_name+
        " how often would you like to do this habit?",components=comp)
        # await ctx.send(content="Creating a habit named "+habit_name+
        # " how often would you like to do this habit?"
        # "\n1)Every day\n2)Specific Days of the week"
        # "\n3)Days per period\n4)Every n days")

        msg = await self.bot.wait_for('message', check=check)        
        
        #get the datetime of gm
        gm = time.gmtime()
        now = datetime.fromtimestamp(mktime(gm))
        
        habit = {
            "name": habit_name.lower(),
            "Discription": None,
            "ReminderText": None,
            "GoalNumber" : None, #for user inputing a number goal
            "Creation":now,
            "Start": None, #day the habit should start
            "Reminder": False, #reminders on or off
            "ReminderTime": None, #Time of day the reminder should be sent
            "Period":None, #days per period
            "Category": None,#defaults to daily (2 for month, 3 year)
            "Days":None, #days of week to set for
            "Frequency": None #repeat every Frequencey days
        }
        var_type = {
            "name": "string",
            "Discription": "string",
            "ReminderText": "string",
            "GoalNumber" : "int", #for user inputing a number goal
            "Creation":"string",
            "Start" : "string",
            "Reminder": "boolean", #reminders on or off
            "ReminderTime": "string",
            "Period":"int", #days per period
            "Category": "int",#defaults to daily (2 for month, 3 year)
            "Days":"string", #days of week to set for
            "Frequency": "int" #repeat every Frequencey days
        }

        if msg.content == "1" or "every day" in msg.content.lower():
            habit["Category"] = 1
        elif msg.content == "2" or "Specific Days of the week" in msg.content.lower():
            await ctx.send(content="What days of the week?"
            "\n[1)Mon 2)Tue 3)Wed 4)Thu 5)Fri 6)Sat 7)Sun]")
            allowed_input_days = [["1","mon"],["2","tue"],["3","wed"],["4","thu"],["5","fri"],["6","sat"],["7","sun"]]

            msg = await self.bot.wait_for('message', check=check)
            habit["Days"] = ""
            for i in allowed_input_days:
                if(i[0] in msg.content or i[1] in msg.content.lower()):
                    habit["Days"]+="1"
                else:
                    habit["Days"]+="0"
        elif(msg.content == "3" or "period" in msg.content.lower()):
            await ctx.send(content="What would you like the period to be?\n1)Week 2)Month 3)Year")
            msg = await self.bot.wait_for('message', check=check)
            arr = ["Week","Month","Year"]
            ptype = 1
            if "1" in msg.content or "week" in msg.content.lower():
                habit["Category"] = 1
            if "2" in msg.content or "month" in msg.content.lower():
                habit["Category"] = 2
                ptype=2
            if "3" in msg.content or "year" in msg.content.lower():
                habit["Category"] = 3
                ptype = 3

            await ctx.send(content="How many times per "+ arr[ptype]+" would you like to do this habit?\n[1,2,3,...]")

            msg = await self.bot.wait_for('message',check=check)
            habit["Period"] = int(msg.content)
        elif(msg.content == "4" or "every" in msg.content.lower()):
            await ctx.send(content="How many days?\n[1,2,3,...]")
            msg = await self.bot.wait_for('message',check=check)
            habit["Frequency"] = int(msg.content)

        await ctx.send(content="Would you like to set a reminder for this habit?(y/n)")
        msg = await self.bot.wait_for('message', check=check)

        if "y" in msg.content.lower():
            habit["Reminder"] = True
            await ctx.send(content="What time would you like the reminder to be sent?")
            msg = await self.bot.wait_for('message', check=check)  
            time = parse(msg)     
            #get the time and convert it into an hh:mm:ss format
            time = time.strftime("%H:%M:%S")
            habit["ReminderTime"] = parse(msg)
        await ctx.send(content="Would you like to set a goal number for this habit?(y/n)")
        msg = await self.bot.wait_for('message', check=check)        
        if "y" in msg.content.lower():
            await ctx.send(content="What would you like that number to be?")
            msg = await self.bot.wait_for('message', check=check)
            habit["GoalNumber"] = int(msg.content)                  


        #TODO: allow the user to choose the start time
        habit["Start"] = habit["Creation"]
        string = "insert into habits VALUES("+str(ctx.message.author.id)+","
        for key in habit:
            if habit[key] == None:
                string+="NULL,"
            elif var_type[key] == "string":
                string+="\"" +str(habit[key]) +"\","
            else:
                string+=str(habit[key]) +","
        string = string[:-1]
        string+=")"
        insert = string;
        connection = create_db_connection("localhost", "root", "root54668", "pa")
        try:
          execute_query(connection,insert)
        except:
          print("An error has occured, habit not created")

        await ctx.send(content="Habit "+habit_name+" creatated successfully!")





def setup(bot):
    bot.add_cog(Habit(bot))
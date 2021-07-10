from discord.ext import commands
import time
from datetime import datetime
from time import mktime
import mysql.connector
from mysql.connector import Error
from db import *
from dateutil.parser import parse
from dateutil.tz import gettz

# class Entry:

#     answer = None
#     def __init__(self,prompt,regex,link):
#         self.prompt=prompt 
#         self.regex = regex
#         self.link = link

# title = Entry("What would you like to call the event?","\w")
# start_date = Entry("What day would you like to start?","regex pattern")
# end_date  = Entry("What day would you like to end?","")
# all_day    = Entry("Is this event all day?","regex pattern")
# duration   = Entry("How long is this event?","regex pattern")
# recurring  = Entry("Is this event recurring?","regex pattern")
# recurrence_pattern = Entry( "What day would you like to start?","regex pattern")
# reminder   = Entry( "Would you like to turn reminders on?","regex pattern")
# description = Entry("Would you like to create a discription?","regex pattern")


# Event = {
#     "title"     :[["What would you like to call the event?"],[],[]]
#     "start_date":["What day would you like to start?","regex pattern",[]]
#     "end_date"  :[["What day would you like to end?"],[],[]]
#     "all_day"   :["Is this event all day?","regex pattern",[]]
#     "duration"  :["How long is this event?","regex pattern",[]]
#     "recurring" :["Is this event recurring?","regex pattern",[]]
#     "recurrence_pattern": ["What day would you like to start?","regex pattern",[]]
#     "reminder"  : ["Would you like to turn reminders on?","regex pattern",[]]
#     "description":["Would you like to create a discription?","regex pattern",[]]
# }

class Event(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def sanitised_input(prompt, type=)
    @commands.command(
        name='event:',
        description='Used to set up a new event ',
        aliases=['e:']
    )
    async def event(self,ctx):
        while True:

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

        await ctx.send(content="Creating a habit named "+habit_name+
        " how often would you like to do this habit?"
        "\n1)Every day\n2)Specific Days of the week"
        "\n3)Days per period\n4)Every n days")

        msg = await self.bot.wait_for('message', check=check)        
        
        #get the datetime of gm
        gm = time.gmtime()
        now = datetime.fromtimestamp(mktime(gm))
        
        Event = {
            "Title" : habit_name.lower(),
            "StartDateUTC" : None,
            "EndDateUTC" : None,
            "IsAllDay" : False,
            "Duration" : None,
            "isRecurring" : True,
            "RecurrencePattern" : "",
            "Reminder" : False,
            "Description" : None
        }
        EventType = {
            "Title" : "string",
            "StartDateUTC" : "string",
            "EndDateUTC" : "string",
            "IsAllDay" : "boolean",
            "Duration" : "int",
            "isRecurring" : "boolean",
            "RecurrencePattern" : "string",
            "Reminder" : "boolean",
            "Description" : "string"
        }
        Habit = {
            "Goal" = None,
            "Period" = False,
            "PeriodPattern" = None,
            "reminderTime" = None,
            "GoalPostFix" = None
        }
        HabitType = {
            "Goal" = "int",
            "Period" = "boolean",
            "PeriodPattern" = "string",
            "reminderTime" = "string",
            "GoalPostFix" = "string"
        }


        if msg.content == "1" or "every day" in msg.content.lower():
            Event["RecurrencePattern"] = "RRULE:FREQ=DAILY;INTERVAL=1"
        elif msg.content == "2" or "Specific Days of the week" in msg.content.lower():
            await ctx.send(content="What days of the week?"
            "\n[1)Mon 2)Tue 3)Wed 4)Thu 5)Fri 6)Sat 7)Sun]")
            allowed_input_days = [["1","mon"],["2","tue"],["3","wed"],["4","thu"],["5","fri"],["6","sat"],["7","sun"]]

            msg = await self.bot.wait_for('message', check=check)
            Event["RecurrencePattern"] = "RRULE:FREQ=WEEKLY;WKST=SU;BYDAY="
            for i in allowed_input_days:
                if(i[0] in msg.content or i[1] in msg.content.lower()):
                    Event["RecurrencePattern"] +=i[1].upper() + ","

            #remove extra comma
            Event["RecurrencePattern"] = Event["RecurrencePattern"][:-1]
        elif(msg.content == "3" or "period" in msg.content.lower()):

            Habit["Period"] = True

            await ctx.send(content="What would you like the period to be?\n1)Week 2)Month 3)Year")
            msg = await self.bot.wait_for('message', check=check)
            arr = ["Week","Month","Year"]
            ptype = 1
            if "1" in msg.content or "week" in msg.content.lower():
                Event["RecurrencePattern"] = "RRULE:FREQ=WEEKLY"
            if "2" in msg.content or "month" in msg.content.lower():
                Event["RecurrencePattern"] = "RRULE:FREQ=MONTHLY"
                ptype=2
            if "3" in msg.content or "year" in msg.content.lower():
                Event["RecurrencePattern"] = "RRULE:FREQ=YEARLY"
                ptype = 3

            await ctx.send(content="How many times per "+ arr[ptype]+" would you like to do this habit?\n[1,2,3,...]")

            msg = await self.bot.wait_for('message',check=check)
            Habit["Period"] = Event["RecurrencePattern"] + ";COUNT=" int(msg.content)
        elif(msg.content == "4" or "every" in msg.content.lower()):
            await ctx.send(content="How many days?\n[1,2,3,...]")
            msg = await self.bot.wait_for('message',check=check)
            Event["RecurrencePattern"] = "RRULE:FREQ=DAILY;INTERVAL=" + msg.content

        await ctx.send(content="Would you like to set a reminder for this habit?(y/n)")
        msg = await self.bot.wait_for('message', check=check)

        if "y" in msg.content.lower():
            Event["Reminder"] = True
            await ctx.send(content="What time would you like the reminder to be sent?")
            msg = await self.bot.wait_for('message', check=check)  
            time = parse(msg)     
            #get the time and convert it into an hh:mm:ss format
            time = time.strftime("%H:%M:%S")
            Habit["ReminderTime"] = parse(msg)
        await ctx.send(content="Would you like to set a goal number for this habit?(y/n)")
        msg = await self.bot.wait_for('message', check=check)        
        if "y" in msg.content.lower():
            await ctx.send(content="What would you like that number to be?")
            msg = await self.bot.wait_for('message', check=check)
            Habit["Goal"] = int(msg.content)           

            await ctx.send(content="What is the postfix?")
            msg = await self.bot.wait_for('message', check=check)
            Habit["GoalPostFix"] = msg.content

        #TODO: allow the user to choose the start time
        Event["StartDateUTC"] = now
        string = "insert into habits VALUES("+str(ctx.message.author.id)+","

        for key in Event:
            if Event[key] == None:
                string+="NULL,"
            elif var_type[key] == "string":
                string+="\"" +str(Event[key]) +"\","
            else:
                string+=str(Event[key]) +","
        string = string[:-1]
        string+=")"
        insert1 = string;

        string = "insert into habits VALUES("+str(ctx.message.author.id)+","
        for key in Habit:
            if Habit[key] == None:
                string+="NULL,"
            elif var_type[key] == "string":
                string+="\"" +str(Habit[key]) +"\","
            else:
                string+=str(Habit[key]) +","
        string = string[:-1]
        string+=")"
        insert2 = string;
        connection = create_db_connection("localhost", "root", "root54668", "pa")
        try:
          execute_query(connection,insert1)
          execute_query(connection,insert2)
        except:
          print("An error has occured, habit not created")

        await ctx.send(content="Habit "+habit_name+" creatated successfully!")


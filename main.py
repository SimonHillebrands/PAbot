from discord.ext import commands
import os
import json
import mysql.connector
from mysql.connector import Error
from db import *


connection = create_db_connection("localhost", "root", "root", "pa")

users= []
class User:
    def __init__(self,id,name,nickname,timezone):
        self.name = name
        self.id = id 
        self.nickname = nickname
        self.timezone = timezone
    # def addHabits(self,habits):
    #     self.habits = habits

reminders = []

bot = commands.Bot(                         
    command_prefix='',              
    description='A personal assistant bot', 
    owner_id=374886124126208000,           
    case_insensitive=True                   
)
bot.reminders = 0;

@bot.check
async def check_user(ctx):
    query = "SELECT * from users WHERE id =" + str(ctx.message.author.id)
    def check(ms):
        return ms.channel == ctx.message.channel and ms.author == ctx.message.author and ms.author != bot.user
    flag = len(read_query(connection,query))
    if(flag == 0):
        nickname = None
        zone = -4
        await ctx.send(content="You are not currently a user, would you like to sign up?(y/n)")
        msg = await bot.wait_for('message', check=check) 
        if(msg.content =="y"):
            await ctx.send(content="Would you like to set a nickname or should I just call you "+ctx.message.author.name+"?(y/n)")
            msg = await bot.wait_for('message', check=check)
            if(msg.content == "y"):
                await ctx.send(content="What would you like me to call you?")
                msg = await bot.wait_for('message', check=check)
            await ctx.send(content="What time zone would you like to use?(EST,PST...)")
            msg = await bot.wait_for('message', check=check)
            zone = timezones[msg.content.upper()]
            if(nickname == None):
                nickname = "NULL"
            else:
                nickname = "\"" + nickname + "\""
            query = "INSERT INTO users values("+str(ctx.message.author.id)+",\""+ctx.message.author.name+"\","+nickname+","+str(zone)+");"
            execute_query(connection,query)
            return True
        else:
            await ctx.send(content="OK")
            return False
    else:
        return True


cogs = ['cogs.basic','cogs.sleep','cogs.log','cogs.request','cogs.habit']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    #users = addUserData()
    for cog in cogs:
        bot.load_extension(cog)
    return
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    ctx = await bot.get_context(message)
    await bot.process_commands(message)#process the message if user



# def generateReminders():
#     for user in users:
#         if(user.habits["timeInfo"]["Category"] == "Daily"):
#             hours = [8,20,12,16]
#             frequency = user.habits["timeInfo"]["Frequency"]
#             for i in range(frequency):
#                 reminders.append(user["User"])
# # async def checkReminders():
# #    for user in users:
# # loop = asyncio.get 


# bot.add_listener(check_user,'on_join')

# with open("Users\\users.txt", "w") as f:
#     for u in users:
#         f.write(u +"\n")

bot.run('NzQ3MjkxNjc5ODE1NDk5ODI5.X0MvnA.BukSKk_8vetCFlkHnyFwF8hSjhQ', bot=True, reconnect=True)
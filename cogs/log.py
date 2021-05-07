from discord.ext import commands
import time
from datetime import datetime
from time import mktime
import mysql.connector
from mysql.connector import Error
from db import *

class Log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        name='log:',
        description='Records all messages that start with this command into a log ',
        aliases=['.']
    )  
    async def log(self, ctx):
        msg = str(ctx.message.content)
        msg = msg.split(' ')

        gm = time.gmtime()
        day = datetime.fromtimestamp(mktime(gm))  

        if(len(msg)>2):
            user_date = msg[2]
            user_date = user_date.split("/")
            if len(user_date)>2:
                day = datetime.strptime(user_date,"%d/%m/%y")
            elif len(user_date) == 2:
                day = datetime.strptime(user_date,"%d/%m")

        else:
            query = "SELECT timeZone from users WHERE id =" + str(ctx.message.author.id)
            offset = len(read_query(connection,query))


        
    bot.add_cog(Log(bot))

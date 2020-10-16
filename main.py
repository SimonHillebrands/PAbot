from discord.ext import commands
import pickle
import os

users=[]


with open("Users\\users.txt", "r") as f:
    for line in f:
        users.append(line.strip())
bot = commands.Bot(                         
    command_prefix='',              
    description='A personal assistant bot', 
    owner_id=374886124126208000,           
    case_insensitive=True                   
)

cogs = ['cogs.basic','cogs.sleep','cogs.log','cogs.request']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    for cog in cogs:
        bot.load_extension(cog)
    return
#if there is not a director for the user, create one
async def check_user(ctx):
    if(ctx.message.author.id not in users):
        id = str(ctx.message.authoer.id)
        users.append(id)
        try:
            os.mkdir(id)
        except OSError:
            print(":(")
    return
bot.add_listener(check_user,'on_join')

with open("Users\\users.txt", "w") as f:
    for u in users:
        f.write(u +"\n")

bot.run('NzQ3MjkxNjc5ODE1NDk5ODI5.X0MvnA.kT_wSPTkSLEgoyKD4oUChb9EQM4', bot=True, reconnect=True)
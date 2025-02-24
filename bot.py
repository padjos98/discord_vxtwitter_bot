#import required libraries and frameworks 
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv, find_dotenv
import vxtwitterlink
import LogonLogoffMessage

#Access the .env file
load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')

#Define the bot for all events and command handling
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#Confrim bot is ready in terminal
@bot.event
async def on_ready():
	print("Bot is ready")


#Message handling when a user sends a messgae
@bot.event
async def on_message(message):
    #Run script to swap x url 
    user_message = message.content
    link = vxtwitterlink.vxtwitterlinkfunc(user_message)
    channelID = message.channel.id
    
	#Determine if the bot needs to delete user's link and replace with their own updated link
    if link == -1:
        return
    else:
        await message.delete()
        general_channel = bot.get_channel(channelID)
        await general_channel.send(content = message.author.mention + '\n' + link, silent=True)

#Handling for User Logon and Logout events
@bot.event
async def on_voice_state_update(member, before, after):
    #Declare variables
    channel = discord.utils.get(bot.get_all_channels(), name='logs')
    #log_channel = bot.get_channel(channel.id)
    log_channel=1342160465395974235
    
    #Send the embedded message
    embed = LogonLogoffMessage.MessageCreate(member, before, after)
    await log_channel.send(embed=embed)

#Run the bot
bot.run(TOKEN)
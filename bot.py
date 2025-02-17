#import required libraries and frameworks 
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv, find_dotenv
import vxtwitterlink

#Access the .env file
load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')

#Declare general channel
GENERAL_CHANNEL_ID=470047029251407875

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
    
	#Determine if the bot needs to delete user's link and replace with their own updated link
    if link == -1:
        return
    else:
        await message.delete()
        general_channel = bot.get_channel(GENERAL_CHANNEL_ID)
        await general_channel.send(link)

#Handling for User Logon
@bot.event
async def on_on_voice_state_update(member):
     print(member)
   


#Run the bot
bot.run(TOKEN)
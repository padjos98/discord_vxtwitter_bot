#import required libraries and frameworks 
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv, find_dotenv
import vxtwitterlink

#Access the .env file
load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')

#Define the bot for all events and command handling
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#Declare general channel
GENERAL_CHANNEL_ID=470047029251407875
general_channel = bot.get_channel(GENERAL_CHANNEL_ID)
VOICE_CHANNEL_ID = 470047029687484416
vocie_channel = bot.get_channel(VOICE_CHANNEL_ID)

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
        await general_channel.send(link)

#Handling for Logon Events
@bot.event
async def on_member_join():
     await vocie_channel.send(1)
#Handling for Logout Events
@bot.event
async def on_member_remove():
	await vocie_channel.send(2)

#Run the bot
bot.run(TOKEN)
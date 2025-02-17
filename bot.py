#import required libraries and frameworks 
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv, find_dotenv
import vxtwitterlink

#Access the .env file
load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('GENERAL_CHANNEL_ID')

#Define the bot for all events and command handling
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#Confrim bot is ready in terminal
@bot.event
async def on_ready():
	print("Bot is ready")


#Message handling when a user sends a messgae
@bot.event
async def on_message(message):
		user_message = message.content
		link = vxtwitterlink.vxtwitterlinkfunc(user_message)

		if user_message == -1:
			print("Invalid Link")
		else:
			print(link)
			
#Run the bot
bot.run(TOKEN)
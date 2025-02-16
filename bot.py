#import required libraries and frameworks 
from discord.ext import commands
import discord
from dotenv import load_dotenv
from pathlib import Path
import vxtwitterlink

#Access the .env file
env_path = Path(__file__).parent.parent / 'vxtwitterbot' / '.env'
load_dotenv(env_path)
TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('GENERAL_CHANNEL_ID', '!')

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
		print(link)

#Run the bot
bot.run(TOKEN)
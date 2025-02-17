#import required libraries and frameworks 
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv, find_dotenv
import vxtwitterlink

#Access the .env file
load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')

#Declare channel ID's
GENERAL_CHANNEL_ID = 470047029251407875
LOG_CHANNEL_ID = 1335751007812059176

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
        await general_channel.send(message.author.mention + '\n' + link)

#Handling for User Logon and Logout events
@bot.event
async def on_voice_state_update(member, before, after):
    #Declare variables
    current_user = str(member)
    profile_pic = member.display_avatar
    sep = '#'
    current_user = current_user.split(sep, 1)[0]
    log_channel = bot.get_channel(LOG_CHANNEL_ID)

    #Create the embedded message
    embedded_message = discord.Embed(
        title="Sample Embed",
        description="This is a description of the embed message.",
        color=discord.Color.blue()
    )

    # Add fields to the embed
    embedded_message.add_field(name="Field 1", value="This is the value for Field 1", inline=False)
    embedded_message.add_field(name="Field 2", value="This is the value for Field 2", inline=True)
    embedded_message.add_field(name="Field 3", value="This is the value for Field 3", inline=True)

    # Add footer and other elements
    embedded_message.set_footer(text="This is a footer")
    embedded_message.set_author(name="Author Name", icon_url="https://example.com/author_icon.png")
    embedded_message.set_thumbnail(url="https://example.com/thumbnail.png")
    embedded_message.set_image(url="https://example.com/image.png")

    #Send the embedded message
    await log_channel.send(embedded_message)

#Run the bot
bot.run(TOKEN)
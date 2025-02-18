#import required libraries and frameworks 
from discord.ext import commands
import discord
from datetime import datetime

def MessageCreate(member, before, after):
    #Declare variables
    sep = '#'
    current_user = str(member).split(sep, 1)[0]
    profile_pic = member.display_avatar
    now = datetime.now()
    current_channel = after.channel
    previous_channel = before.channel
    message_color = 0xff0000
    voice_state = ""

    #Determine if user joined, disconnected or switched channels and set color, current channel, and voice state appropriately 
 
    if current_channel == None:
        current_channel = before.channel
        message_color = 0xff0000
        voice_state = "Voice Leave"
    elif previous_channel == None:
        current_channel = after.channel
        message_color = 0x00ff00
        voice_state = "Voice Join"
    else:
        current_channel = after.channel
        message_color = 0xffff00
        voice_state = "Voice Switch"

    #Create the embedded message
    embed = discord.Embed(color=message_color)

    #Add fields to the embed
    #embed.set_thumbnail(url=profile_pic)
    embed.add_field(name=current_user, value="", inline=True)
    embed.add_field(name=voice_state, value="", inline=False)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Channel", value=current_channel.mention, inline=True)
    embed.add_field(name=now.strftime("%m/%d/%y %H:%-I:%S %p"), value="", inline=False)  
    return embed 
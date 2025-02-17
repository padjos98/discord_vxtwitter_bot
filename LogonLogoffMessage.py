#import required libraries and frameworks 
from discord.ext import commands
import discord

def MessageCreate(member):
#Declare variables
    current_user = str(member)
    profile_pic = member.display_avatar
    sep = '#'
    current_user = current_user.split(sep, 1)[0]

    #Create the embedded message
    embed = discord.Embed()

    #Add fields to the embed
    #embed.set_thumbnail(url=profile_pic)
    embed.add_field(name=current_user, value="", inline=True)
    embed.add_field(name="Voice Leave", value="", inline=False)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Channel", value="", inline=True)
    embed.add_field(name="Time", value="", inline=False)
    #Send the embedded message
    
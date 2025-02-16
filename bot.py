from discord.ext import commands
import discord
import vxtwitterlink

BOT_TOKEN = "MTM0MDU1MTM5NzE2MjA5NDU5Mg.GGW5fI.9cInpJz-elDTpstpSF4nhF81ysCCPc07YP_gnc"
GENERAL_CHANNEL_ID = 470047029251407875

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
	print("Bot is ready")


@bot.event
async def on_message(message):
		user_message = message.content
		link = vxtwitterlink.vxtwitterlinkfunc(user_message)
		print(link)

bot.run(BOT_TOKEN)
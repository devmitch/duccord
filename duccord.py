import discord
import asyncio
from discord.ext import commands
from settings import BOT_TOKEN
from modules import db as db
from modules import daily

# Initialise connection to database
client = db.start()
# Initialise discord bot
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("Bot ready!")
    bot.loop.create_task(daily.daily_ducc(bot))


@bot.command(pass_context=True)
async def hi(context):
    file = discord.File("ducc-hi.jpeg", filename="image.jpeg")
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_image(url="attachment://image.jpeg")
    embed.set_footer(text="Quacc.")
    await context.send(content="Hi %s!" % context.message.author.mention, file=file, embed=embed)


@bot.command(pass_contest=True)
async def echo(context, *args):
    if not args:
        await context.send("You didn't type anything for me to echo...")
    else:
        await context.send(" ".join(args[:]))


@bot.command(pass_context=True)
async def subscribe(context):
    await daily.toggle_subscribe(bot, context.message.author.id)

bot.run(BOT_TOKEN)

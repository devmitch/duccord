import discord
from discord.ext import commands
from settings import BOT_TOKEN

bot = commands.Bot(command_prefix='$')


@bot.command(pass_context=True)
async def hi(context):
    file = discord.File("ducc-hi.jpeg", filename="image.jpeg")
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_image(url="attachment://image.jpeg")
    embed.set_footer(text="Quacc.")
    await context.send(content="Hi %s!" % context.message.author.mention, file=file, embed=embed)


@bot.command(pass_contest=True)
async def echo(context, string=""):
    if not string:
        await context.send("You didn't type anything for me to echo...")
    else:
        await context.send(string)

bot.run(BOT_TOKEN)

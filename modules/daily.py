from datetime import datetime, timedelta
from .db import *
import asyncio
import requests
import discord

async def toggle_subscribe(bot, user_id):
    client = start()
    db = init(client, 'daily')
    subscriptions = collection_init(db, 'subscriptions')
    entry = find_one(subscriptions, {'user_id': user_id})
    if not entry:
        insert_one(subscriptions, {'user_id': user_id, 'subscribed': 1})
        user = bot.get_user(user_id)
        await user.send("Subscribed to daily ducc pics :)")
    elif not entry['subscribed']:
        update_one(subscriptions, entry, {"$set": {"subscribed": 1}})
        user = bot.get_user(user_id)
        await user.send("Subscribed to daily ducc pics :)")
    else:
        update_one(subscriptions, entry, {"$set": {"subscribed": 0}})
        user = bot.get_user(user_id)
        await user.send("Un-subscribed from daily ducc pics :(")


async def daily_ducc(bot):
    await bot.wait_until_ready()
    print("Starting daily ducc task loop")
    streak = 0
    now = datetime.now()
    wait = (timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)
    print("Waiting ", wait, " seconds until 9am")
    await asyncio.sleep(wait)
    client = start()
    db = init(client, 'daily')
    subscriptions = collection_init(db, 'subscriptions')
    while not bot.is_closed():
        print("Sending out ducc pics!")
        streak += 1
        for entry in find(subscriptions):
            if entry['subscribed'] == 1:
                user = bot.get_user(entry['user_id'])
                req = requests.get('https://random-d.uk/api/random')
                image_url = req.json()['url']
                embed = discord.Embed(colour=discord.Colour.gold())
                embed.set_image(url=image_url)
                embed.set_footer(text="Powered by random-d.uk | Type $subscribe to toggle subscription")
                await user.send(content="Here is your daily ducc!", embed=embed)
        print("Finished sending ducc pics. Waiting until tomorrow to send them again!")
        await asyncio.sleep(60*60*24)

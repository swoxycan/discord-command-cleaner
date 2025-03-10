import discord
import aiohttp
import asyncio
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    TOKEN = config['token']
    APPLICATION_ID = config['application_id']

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

async def remove_slash_commands():
    await bot.wait_until_ready()
    
    url = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands"
    headers = {
        "Authorization": f"Bot {TOKEN}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                commands = await response.json()
                for cmd in commands:
                    cmd_id = cmd["id"]
                    del_url = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands/{cmd_id}"

                    async with session.delete(del_url, headers=headers) as del_response:
                        if del_response.status in [200, 204]:
                            print(f"✅ Komut silindi: {cmd['name']}")
                        elif del_response.status == 429:
                            retry_after = int(del_response.headers.get("Retry-After", 1))
                            print(f"⚠️ Rate limit aşıldı! {retry_after} saniye bekleniyor...")
                            await asyncio.sleep(retry_after)
                        else:
                            print(f"⚠️ Silme hatası: {del_response.status}")

                    await asyncio.sleep(1)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")
    await remove_slash_commands()
    await bot.close()

bot.run(TOKEN)

import discord
import aiohttp
import asyncio
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    TOKEN = config['token']
    APPLICATION_ID = config['application_id']

intents = discord.Intents.default()
intents.guilds = True
bot = discord.Client(intents=intents)

async def remove_slash_commands():
    await bot.wait_until_ready()
    
    global_url = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands"
    guild_url_template = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/guilds/{{guild_id}}/commands"
    
    headers = {
        "Authorization": f"Bot {TOKEN}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(global_url, headers=headers) as response:
            if response.status == 200:
                commands = await response.json()
                if commands:
                    print(f"🔍 Toplam {len(commands)} global komut bulundu. Silme işlemi başlıyor...")
                    for cmd in commands:
                        cmd_id = cmd["id"]
                        del_url = f"{global_url}/{cmd_id}"
                        async with session.delete(del_url, headers=headers) as del_response:
                            if del_response.status in [200, 204]:
                                print(f"✅ Global komut silindi: {cmd['name']}")
                            elif del_response.status == 429:
                                retry_after = int(del_response.headers.get("Retry-After", 1))
                                print(f"⚠️ Rate limit aşıldı! {retry_after} saniye bekleniyor...")
                                await asyncio.sleep(retry_after)
                            else:
                                error_data = await del_response.json()
                                error_message = error_data.get('message', 'Bilinmeyen hata')
                                print(f"⚠️ Silme hatası (Kod: {del_response.status}): {error_message}")
                            await asyncio.sleep(1)

        for guild in bot.guilds:
            guild_url = guild_url_template.format(guild_id=guild.id)
            async with session.get(guild_url, headers=headers) as response:
                if response.status == 200:
                    commands = await response.json()
                    if commands:
                        print(f"🔍 {guild.name} sunucusunda {len(commands)} komut bulundu. Silme işlemi başlıyor...")
                        for cmd in commands:
                            cmd_id = cmd["id"]
                            del_url = f"{guild_url}/{cmd_id}"
                            async with session.delete(del_url, headers=headers) as del_response:
                                if del_response.status in [200, 204]:
                                    print(f"✅ Guild komutu silindi: {cmd['name']} ({guild.name})")
                                elif del_response.status == 429:
                                    retry_after = int(del_response.headers.get("Retry-After", 1))
                                    print(f"⚠️ Rate limit aşıldı! {retry_after} saniye bekleniyor...")
                                    await asyncio.sleep(retry_after)
                                else:
                                    error_data = await del_response.json()
                                    error_message = error_data.get('message', 'Bilinmeyen hata')
                                    print(f"⚠️ Silme hatası (Kod: {del_response.status}): {error_message}")
                                await asyncio.sleep(1)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")
    await remove_slash_commands()
    await bot.close()

bot.run(TOKEN)

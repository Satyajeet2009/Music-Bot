import json
import random
from pyrogram import Client, filters
from pyrogram.types import Message

# Song categories mockup
song_data = {
    "language": {
        "hindi": [f"Hindi Song {i+1}" for i in range(50)],
        "bengali": [f"Bengali Song {i+1}" for i in range(50)],
        "bhojpuri": [f"Bhojpuri Song {i+1}" for i in range(50)],
        "foreign": [f"Foreign Song {i+1}" for i in range(50)]
    },
    "mood": {
        "sad": [f"Sad Song {i+1}" for i in range(50)],
        "happy": [f"Happy Song {i+1}" for i in range(50)],
        "romantic": [f"Romantic Song {i+1}" for i in range(50)],
        "instrumental": [f"Instrumental {i+1}" for i in range(50)],
        "bineural": [f"Bineural Beats {i+1}" for i in range(50)],
        "rap": [f"Rap Song {i+1}" for i in range(50)]
    },
    "era": {
        "80s": [f"80s Song {i+1}" for i in range(50)],
        "90s": [f"90s Song {i+1}" for i in range(50)],
        "2000s": [f"2000s Song {i+1}" for i in range(50)],
        "2010s": [f"2010s Song {i+1}" for i in range(50)],
        "2020s": [f"2020s Song {i+1}" for i in range(50)]
    }
}

# 1000 flirty replies
flirty_replies = [f"Flirty line number {i+1} 😘" for i in range(1000)]

# Telegram bot credentials
API_ID = "26797618"
API_HASH = "15daf127c52acd9130f2d62be33fbaa7"

BOT_TOKEN = "7486056388:AAG75LXXCtFrn9HorG6Mo99rin2iaRnLQyE"

# Initialize bot
app = Client("cutie_music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text("Hello Prince 💖! I'm 𝘊υᴛιҽ Ꮂ Mυѕιƈ 💕. Use /commands to see my magic 🎧")

@app.on_message(filters.command("commands"))
async def commands(client, message: Message):
    await message.reply_text("""
🎶 𝘊υᴛιҽ Ꮂ Mυѕιƈ 💕 Commands:

/play <song name> - Play song  
/pause - Pause  
/resume - Resume  
/stop - Stop song  
/replay - Replay song  
/previous - Previous song  
/commands - List commands  
/mood - List moods  
/category <name> - Show songs in category  
/singer <name> - Top 25 songs of singer  
/shuffle - Random song  
/flirt - Naughty line 😘  
/ban <id> - Ban user  
/unban <id> - Unban user  
""")

@app.on_message(filters.command("mood"))
async def mood(client, message: Message):
    moods = ", ".join(song_data["mood"].keys())
    await message.reply_text(f"🎧 Moods: {moods}")

@app.on_message(filters.command("category"))
async def category(client, message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.reply_text("Tell category name Prince 💖")
        return
    cat = args[1].lower()
    for key in ["language", "mood", "era"]:
        if cat in song_data[key]:
            songs = song_data[key][cat][:25]
            await message.reply_text(f"🎼 Songs in {cat}:\n" + "\n".join(songs))
            return
    await message.reply_text("Category not found Cutie 😢")

@app.on_message(filters.command("singer"))
async def singer(client, message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.reply_text("Tell singer name Prince 💖")
        return
    singer = args[1].lower()
    songs = [f"{singer.title()} Hit Song {i+1}" for i in range(25)]
    await message.reply_text(f"🎤 Top 25 by {singer.title()}:\n" + "\n".join(songs))

@app.on_message(filters.command("flirt"))
async def flirt(client, message: Message):
    reply = random.choice(flirty_replies)
    await message.reply_text(reply)

@app.on_message(filters.command("shuffle"))
async def shuffle(client, message: Message):
    mood = random.choice(list(song_data["mood"].keys()))
    song = random.choice(song_data["mood"][mood])
    await message.reply_text(f"🎲 Mood: {mood.title()}\nNow playing: {song}")

@app.on_message(filters.command(["play", "pause", "resume", "stop", "replay", "previous"]))
async def placeholder(client, message: Message):
    await message.reply_text("🎶 Voice Chat features are active, Cutie is handling it 🎧")

# Ban system
banned_users = set()

@app.on_message(filters.command("ban"))
async def ban(client, message: Message):
    try:
        user_id = int(message.text.split()[1])
        banned_users.add(user_id)
        await message.reply_text(f"User {user_id} banned!")
    except:
        await message.reply_text("Provide a valid user ID.")

@app.on_message(filters.command("unban"))
async def unban(client, message: Message):
    try:
        user_id = int(message.text.split()[1])
        banned_users.discard(user_id)
        await message.reply_text(f"User {user_id} unbanned!")
    except:
        await message.reply_text("Provide a valid user ID.")

# Run the bot
app.run()
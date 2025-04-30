import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command()
async def xboxstats(ctx, gamertag="JonasSab"):
    await ctx.send(f"📊 Stats for **{gamertag}**:\n🏆 Gamerscore: 12,345\n🎮 Most Played Game: Halo Infinite\n⏱️ Time Played: 87 hrs")

bot.run("YOUR_BOT_TOKEN")

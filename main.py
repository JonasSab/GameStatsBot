import discord
from discord import app_commands
from discord.ext import commands

# Define the bot with slash command support
intents = discord.Intents.default()
intents.message_content = True  # Required for message content access
bot = commands.Bot(command_prefix="!", intents=intents)

# This is where we define your /xboxstats command
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Slash command for /xboxstats
@bot.tree.command(name="xboxstats", description="Fetch Xbox stats for a user")
async def xboxstats(interaction: discord.Interaction, username: str):
    # You can replace the following logic with actual Xbox stat fetching code
    # For now, it just replies with a placeholder message
    await interaction.response.send_message(f"Fetching stats for Xbox user: {username}")

# Sync the commands once after the bot starts
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync commands with Discord
    print(f'Bot is ready. Logged in as {bot.user}')

# Run the bot with your token
bot.run("YOUR_BOT_TOKEN")

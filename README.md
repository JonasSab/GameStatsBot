# 🎮 Xbox Stats Discord Bot (Work in Progress)

Fetch Xbox Live player stats directly within Discord using slash commands!  
This bot is currently **under development** and does not yet support full stat fetching — but you can follow along or contribute.

---

## 📌 Features (Planned)

- ✅ Slash command support: `/xboxstats <gamertag>`
- 🔄 Fetch Xbox Live stats like Gamerscore, recent games, and achievements (in progress)
- 🛡️ Secure OAuth2-based Xbox Live authentication (coming soon)
- 🧠 Smart error messages and username checks

---

## 🚧 Current Status

This project is **work in progress**. The command is implemented and responds to input, but actual Xbox Live API integration and data fetching is not yet completed. The `/xboxstats` command currently returns a placeholder message.

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/JonasSab/GameStatsBot.git
cd GameStatsBot
```

### 2. Install Dependencies

Make sure you’re using Python 3.9 or higher (preferably 64-bit), and install required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install discord.py
```

### 3. Create a Discord Bot

- Go to the [Discord Developer Portal](https://discord.com/developers/applications)
- Create a new application
- Go to the **Bot** tab → Click “Add Bot”
- Enable the following:
  - ✅ `MESSAGE CONTENT INTENT`
  - ✅ `SERVER MEMBERS INTENT`
- Under **OAuth2 > URL Generator**:
  - Scopes: `bot`, `applications.commands`
  - Bot Permissions: `Send Messages`, `Use Application Commands`

Copy the generated URL, paste it into your browser, and invite the bot to your server.

### 4. Configure Environment Variables

You can either:
- Set environment variables directly, or
- Create a `.env` file and use the `dotenv` module

Basic config:

```python
TOKEN = "your-discord-bot-token-here"
```

### 5. Run the Bot

```bash
python main.py
```

---

## 💬 Usage

In any Discord server where the bot is installed:

```bash
/xboxstats JonasSab
```

Expected result (currently returns a placeholder response):

```
Looking up stats for JonasSab... (Feature coming soon!)
```

---

## 📈 Planned Xbox API Integration

To fetch real Xbox Live stats, you will eventually need:
- Xbox Developer Program membership (via [ID@Xbox](https://www.xbox.com/en-us/developers/id) or [Xbox Creators Program](https://www.xbox.com/en-US/developers/creators-program))
- Registered app with proper scopes:
  - `XboxLive.signin`
  - `XboxLive.offline_access`

Integration with PlayFab (optional) is also being explored.

---

## 🧠 Example Code Snippet

```python
@tree.command(name="xboxstats", description="Get stats for an Xbox user")
@app_commands.describe(username="Enter the Xbox username")
async def xboxstats(interaction: discord.Interaction, username: str):
    await interaction.response.send_message(f"Looking up stats for {username}... (Feature coming soon!)")
```

---

## 🛠️ Tech Stack

- Python 3.9+
- discord.py (with `app_commands` for slash commands)
- Future: Xbox Live REST API, OAuth2, PlayFab


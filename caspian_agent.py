import os
from dotenv import load_dotenv
from caspian import Caspian
from crewai_client import ask_careerpilot

load_dotenv()

# ==============================
# Caspian
# ==============================

cx = Caspian(
    api_key=os.getenv("CASPIAN_API_KEY"),
    base_url=os.getenv(
        "CASPIAN_BASE_URL",
        "https://api.trycaspianai.com"
    )
)

# ==============================
# Telegram
# ==============================

cx.channels.add(
    "telegram",
    bot_token=os.getenv("TELEGRAM_BOT_TOKEN")
)

# ==============================
# Discord
# ==============================

print(
    "Discord token loaded:",
    bool(os.getenv("DISCORD_BOT_TOKEN"))
)

discord_connection = cx.channels.add(
    "discord",
    display_name="CareerPilot AI",
    bot_token=os.getenv("DISCORD_BOT_TOKEN")
)

print("Discord connection:")
print(discord_connection)

# ==============================
# ONE HANDLER FOR ALL CHANNELS
# ==============================

@cx.on_message({
    "overlap": "queue",
    "ack": "CareerPilot is thinking..."
})
def handle(thread, msg, ctx):

    print(f"\nUser Message: {msg.text}")

    try:
        # Send message to your existing CrewAI agent
        response = ask_careerpilot(msg.text)

        # Send CrewAI response back to the same channel
        thread.post(response)

        print("✓ Response sent")

    except Exception as e:
        print(f"❌ Error: {e}")

        thread.post(
            "Sorry, I couldn't process your request right now."
        )


# ==============================
# START CASPIAN
# ==============================

print("\n===================================")
print("       CareerPilot AI")
print("===================================")
print("Telegram: Connected")
print("Discord: Connected")
print("Caspian: Starting...")
print("===================================\n")

cx.run()
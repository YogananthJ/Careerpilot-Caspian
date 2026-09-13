import os
from dotenv import load_dotenv
from caspian import Caspian
from crewai_client import ask_careerpilot


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# TERMINAL DESIGN
# ============================================================

print("\n")
print("╔══════════════════════════════════════════════════════════╗")
print("║                                                          ║")
print("║                  🚀 CAREERPILOT AI                       ║")
print("║                                                          ║")
print("║          AI-Powered Career Mentor for Students           ║")
print("║                                                          ║")
print("╚══════════════════════════════════════════════════════════╝")
print()


# ============================================================
# CASPIAN INITIALIZATION
# ============================================================

print("┌──────────────────────────────────────────────────────────┐")
print("│ Initializing Caspian...                                  │")
print("└──────────────────────────────────────────────────────────┘")

cx = Caspian(
    api_key=os.getenv("CASPIAN_API_KEY"),
    base_url=os.getenv(
        "CASPIAN_BASE_URL",
        "https://api.trycaspianai.com"
    )
)

print("✓ Caspian initialized")


# ============================================================
# TELEGRAM CONNECTION
# ============================================================

print("\n┌──────────────────────────────────────────────────────────┐")
print("│ Connecting Telegram...                                   │")
print("└──────────────────────────────────────────────────────────┘")

cx.channels.add(
    "telegram",
    bot_token=os.getenv("TELEGRAM_BOT_TOKEN")
)

print("✓ Telegram connected")


# ============================================================
# DISCORD CONNECTION
# ============================================================

print("\n┌──────────────────────────────────────────────────────────┐")
print("│ Connecting Discord...                                    │")
print("└──────────────────────────────────────────────────────────┘")

print(
    "Discord token loaded:",
    bool(os.getenv("DISCORD_BOT_TOKEN"))
)

discord_connection = cx.channels.add(
    "discord",
    display_name="CareerPilot AI",
    bot_token=os.getenv("DISCORD_BOT_TOKEN")
)

print("✓ Discord connection created")
print("  Connection:", discord_connection)


# ============================================================
# SHARED MESSAGE HANDLER
# ============================================================
#
# Both Telegram and Discord use this SAME handler.
#
# User
#   ↓
# Telegram / Discord
#   ↓
# Caspian
#   ↓
# THIS HANDLER
#   ↓
# CrewAI
#   ↓
# Response
#   ↓
# Original Channel
#
# ============================================================

@cx.on_message({
    "overlap": "queue",
    "ack": "CareerPilot is thinking..."
})
def handle(thread, msg, ctx):

    # --------------------------------------------------------
    # SHOW USER MESSAGE IN TERMINAL
    # --------------------------------------------------------

    print("\n")
    print("══════════════════════════════════════════════════════════")
    print("📩 NEW MESSAGE")
    print("══════════════════════════════════════════════════════════")
    print(f"User: {msg.text}")
    print("──────────────────────────────────────────────────────────")

    try:

        # ----------------------------------------------------
        # SEND USER MESSAGE TO CREWAI
        # ----------------------------------------------------

        print("🧠 CareerPilot is processing with CrewAI...")

        response = ask_careerpilot(msg.text)

        # ----------------------------------------------------
        # SHOW RESPONSE INFORMATION
        # ----------------------------------------------------

        print("✓ CrewAI completed successfully")
        print(f"✓ Response length: {len(response)} characters")

        print("──────────────────────────────────────────────────────────")
        print("🤖 Response preview:")
        print(response[:500])

        # ----------------------------------------------------
        # SEND RESPONSE BACK TO CHANNEL
        # ----------------------------------------------------
        #
        # Discord has a 2000-character message limit.
        #
        # We use 1900 instead of 2000 to leave a small margin.
        #
        # Example:
        #
        # 3659 characters
        #
        # ↓
        #
        # Message 1 = 1900
        # Message 2 = 1759
        #
        # Telegram also accepts these chunks, so the same
        # handler continues to work for both channels.
        #
        # ----------------------------------------------------

        MAX_MESSAGE_LENGTH = 1900

        total_chunks = (
            len(response) + MAX_MESSAGE_LENGTH - 1
        ) // MAX_MESSAGE_LENGTH

        print(
            f"📤 Sending response in {total_chunks} message(s)..."
        )

        for i in range(0, len(response), MAX_MESSAGE_LENGTH):

            chunk = response[
                i:i + MAX_MESSAGE_LENGTH
            ]

            thread.post(chunk)

            print(
                f"  ✓ Sent message {i // MAX_MESSAGE_LENGTH + 1}"
                f"/{total_chunks}"
            )

        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        print("✓ Response sent successfully")
        print("══════════════════════════════════════════════════════════")

    except Exception as e:

        # ----------------------------------------------------
        # ERROR HANDLING
        # ----------------------------------------------------

        print("\n")
        print("❌ ERROR")
        print("──────────────────────────────────────────────────────────")
        print(f"{e}")
        print("──────────────────────────────────────────────────────────")

        thread.post(
            "Sorry, I couldn't process your request right now. "
            "Please try again."
        )


# ============================================================
# START CAREERPILOT
# ============================================================

print("\n")
print("╔══════════════════════════════════════════════════════════╗")
print("║                  SYSTEM STATUS                           ║")
print("╠══════════════════════════════════════════════════════════╣")
print("║                                                          ║")
print("║  🟢 Telegram     : Connected                             ║")
print("║  🟢 Discord      : Connected                             ║")
print("║  🟢 Caspian      : Ready                                 ║")
print("║  🟢 CrewAI       : Ready                                 ║")
print("║                                                          ║")
print("║  CareerPilot AI is now LIVE 🚀                           ║")
print("║                                                          ║")
print("║  Waiting for messages...                                 ║")
print("║                                                          ║")
print("╚══════════════════════════════════════════════════════════╝")
print("\n")


# ============================================================
# START CASPIAN MESSAGE LOOP
# ============================================================

cx.run()
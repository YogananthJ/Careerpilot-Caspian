# CareerPilot AI

### AI-Powered Career Mentor for Students & Freshers

CareerPilot AI is a multi-channel AI career assistant designed to help students and freshers make better career decisions through personalized career guidance, skill-gap analysis, learning roadmaps, resume guidance, and interview coaching.

Built with **CrewAI** for AI reasoning and orchestration and **Caspian SDK** for multi-channel communication, CareerPilot can interact with users through **Telegram and Discord using a shared message handler**.

---

## 🎯 Problem

Students and freshers often face questions such as:

- Which career path should I choose?
- What skills do I need for my target role?
- What should I learn next?
- How do I become job-ready?
- How should I prepare for technical interviews?
- What projects should I build?
- How can I improve my resume?

CareerPilot AI provides a conversational career mentor that can help users answer these questions and create practical next steps based on their goals and background.

---

## 💡 Solution

CareerPilot AI combines an AI-powered career reasoning workflow with a multi-channel communication layer.

The system:

1. Receives a user's message through Telegram or Discord.
2. Routes the message through Caspian.
3. Sends the request to the deployed CrewAI workflow.
4. Classifies the user's intent.
5. Routes the request to the appropriate specialized career agent.
6. Generates a structured response.
7. Sends the response back through the same communication channel.

The same message handler is used across both Telegram and Discord.

---

## ✨ Key Features

### 🎯 Career Guidance

Provides personalized guidance based on a user's:

- Career interests
- Educational background
- Current skills
- Experience
- Career goals

### 📊 Skill-Gap Analysis

Helps users understand:

- Current skill level
- Required skills for a target role
- Missing or weak areas
- Recommended areas for improvement

### 🗺️ Learning Roadmaps

Generates structured learning paths with:

- Topics to learn
- Recommended progression
- Practical learning goals
- Project suggestions
- Career preparation steps

### 📄 Resume Guidance

Provides conversational feedback and suggestions for improving resumes and presenting skills more effectively.

### 🎤 Interview Coaching

Supports interview preparation through:

- Technical interview practice
- Role-specific questions
- Mock interview conversations
- Interview preparation guidance

### 💬 Multi-Channel Communication

CareerPilot is accessible through:

- Telegram
- Discord

Both channels communicate with the same CareerPilot backend through Caspian.

---

# 🏗️ Architecture

```text
                          USER INPUT
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
             ┌─────────────┐     ┌─────────────┐
             │  Telegram   │     │   Discord   │
             │    User     │     │    User     │
             └──────┬──────┘     └──────┬──────┘
                    │                   │
                    └─────────┬─────────┘
                              ▼
                    ┌───────────────────┐
                    │      Caspian      │
                    │ Communication     │
                    │      Layer        │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Shared Message    │
                    │     Handler       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │     CrewAI API    │
                    │                   │
                    │  CareerPilot      │
                    │     Workflow      │
                    └─────────┬─────────┘
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
      Intent Router    Career Advisor    Interview Coach
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                    ┌───────────────────┐
                    │ Response Formatter│
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Response through │
                    │      Caspian      │
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              ┌───────────┐       ┌───────────┐
              │ Telegram  │       │  Discord  │
              │   User    │       │   User    │
              └───────────┘       └───────────┘
```

---

# 🧠 AI Workflow

CareerPilot uses a deployed CrewAI workflow containing specialized components for different stages of the conversation.

### Workflow

```text
User Message
     │
     ▼
Intent Classification
     │
     ▼
Request Routing
     │
     ├───────────────┐
     ▼               ▼
Career Advisor   Interview Coach
     │               │
     └───────┬───────┘
             ▼
     Response Formatter
             │
             ▼
        Final Response
```

This allows CareerPilot to handle different career-related requests instead of treating every conversation as a generic chatbot interaction.

---

# 🔗 Why Caspian?

Caspian is used as the **communication layer** of CareerPilot.

Instead of implementing separate communication logic for each platform, CareerPilot uses Caspian to connect multiple channels to a shared message handler.

```text
Telegram ──┐
           │
Discord ───┼──► Caspian ──► Shared Handler ──► CareerPilot
           │
           └───────────────────────────────────────
```

This architecture allows the same CareerPilot agent to communicate with users across multiple platforms.

Caspian's core design is built around using one handler across multiple communication channels.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| CrewAI | Agent orchestration and AI workflow |
| Caspian SDK | Multi-channel communication |
| Telegram | User communication channel |
| Discord | User communication channel |
| REST API | Communication with deployed CrewAI workflow |
| Requests | HTTP API calls |
| python-dotenv | Environment variable management |

---

# 📁 Project Structure

```text
careerpilot-caspian/
│
├── app.py
├── caspian_agent.py
├── crewai_client.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

### `app.py`

Local command-line entry point for interacting with CareerPilot.

### `crewai_client.py`

Handles communication with the deployed CrewAI workflow.

### `caspian_agent.py`

Connects CareerPilot to Telegram and Discord through the Caspian SDK and contains the shared message handler.

### `requirements.txt`

Contains the Python dependencies required to run the project.

### `.env.example`

Documents the required environment variables without exposing actual credentials.

---

# 🚀 Getting Started

## Prerequisites

Make sure you have:

- Python 3.10+
- A Caspian API key
- A Telegram Bot Token
- A Discord Bot Token
- Access to the deployed CrewAI workflow

---

## 1. Clone the repository

```bash
https://github.com/YogananthJ/Careerpilot-Caspian.git
cd careerpilot-caspian
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the project root.

```env
CREWAI_API_URL=
CREWAI_BEARER_TOKEN=

CASPIAN_API_KEY=
CASPIAN_BASE_URL=https://api.trycaspianai.com

TELEGRAM_BOT_TOKEN=
DISCORD_BOT_TOKEN=
```

Fill these values with your own credentials.

> **Security:** Never commit `.env` or API keys to GitHub. Use `.env.example` as the template for required variables.

---

# ▶️ Running CareerPilot

Start the multi-channel agent:

```bash
python caspian_agent.py
```

You should see a startup message similar to:

```text
===================================
       CareerPilot AI
===================================
Telegram: Connected
Discord: Connected
Caspian: Starting...
===================================
```

Once the process is running, CareerPilot can receive messages through the configured channels.

---

# 💬 Using CareerPilot

## Telegram

Try CareerPilot AI directly on Telegram:

👉 [Launch CareerPilot AI on Telegram](https://t.me/CareerPilotAgent2026_bot)

Search for the configured CareerPilot Telegram bot and send a message such as:

```text
I am a final-year student interested in AI/ML.
I want to become an AI/ML Engineer.
Give me a practical 6-month roadmap.
```

Other examples:

```text
What skills should I improve to become job-ready for AI/ML roles?
```

```text
What projects should I build for an AI/ML Engineer position?
```

```text
Start a mock interview for an AI/ML Engineer fresher role.
```

---

## Discord

Invite the configured CareerPilot bot to a Discord server and send messages such as:

```text
I am preparing for an AI/ML interview.
Can you start a mock interview?
```

The same CareerPilot message handler processes requests from both Telegram and Discord.

---

# 🔄 Caspian Integration

The core Caspian integration is implemented in `caspian_agent.py`.

Telegram and Discord are connected as channels:

```python
cx.channels.add(
    "telegram",
    bot_token=os.getenv("TELEGRAM_BOT_TOKEN")
)

cx.channels.add(
    "discord",
    display_name="CareerPilot AI",
    bot_token=os.getenv("DISCORD_BOT_TOKEN")
)
```

Both channels use a shared message handler:

```python
@cx.on_message({
    "overlap": "queue",
    "ack": "CareerPilot is thinking..."
})
def handle(thread, msg, ctx):
    response = ask_careerpilot(msg.text)
    thread.post(response)
```

This allows CareerPilot to maintain a single application-level message handling flow across multiple channels.

---

# ☁️ Deployment

The CrewAI workflow is deployed through CrewAI's hosted API.

The Caspian communication process can be run locally or deployed to a cloud environment for continuous availability.

For production-style deployment, environment variables should be configured through the hosting platform rather than committed to source control.

---

# 🔐 Security

This project uses environment variables for sensitive credentials.

The following values must never be committed to the repository:

```text
CASPIAN_API_KEY
CREWAI_BEARER_TOKEN
TELEGRAM_BOT_TOKEN
DISCORD_BOT_TOKEN
```

Use `.env.example` to document required configuration without exposing secrets.

---

# 🧪 Tested Channels

CareerPilot has been tested end-to-end through:

- ✅ Telegram
- ✅ Discord

Both channels successfully communicate with the same CareerPilot workflow.

---

# 🌟 Project Highlights

- Multi-channel AI career assistant
- CrewAI-powered agent workflow
- Caspian communication layer
- Telegram + Discord integration
- Shared message handler across channels
- Career guidance and skill-gap analysis
- Learning roadmap generation
- Interview coaching
- Cloud-hosted CrewAI workflow
- Environment-based secret management

---

# 🎯 Future Improvements

Potential future improvements include:

- Resume file upload and automated analysis
- Persistent user profiles and career history
- Personalized job recommendations
- Job-market skill trend analysis
- Progress tracking
- Additional communication channels
- Web-based CareerPilot dashboard
- Automated interview scoring

---

# 👨‍💻 Author

**Yogananth J**

B.Tech — Artificial Intelligence & Machine Learning

CareerPilot AI was developed as an AI agent project using **CrewAI** and **Caspian SDK**.

---

## Acknowledgements

- [Caspian SDK](https://github.com/TryCaspian/caspian-sdk) — Agent communication layer
- CrewAI — AI agent orchestration platform
- Telegram — Messaging platform
- Discord — Community and messaging platform

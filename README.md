# VenueAI 🏟️ - Smart Venue Assistant

> **PromptWars 2025 Hackathon Project**  
> **Vertical: Physical Event Experience**

---

## Problem Statement

Large-scale sporting venues face massive challenges during events:
- Crowds get stuck at main gates with no alternate routes
- Long unpredictable wait times at food stalls and restrooms
- Attendees lost and confused about schedules, gates, and parking
- Emergency situations handled slowly due to poor communication

Attendees spend more time confused and waiting than actually enjoying the event.

---

## Solution: VenueAI

VenueAI is an **AI-powered conversational assistant** for sporting venue attendees. It provides **real-time, personalized guidance** through a simple chat interface accessible on any mobile browser — no app download needed.

---

## How AI Helps Attendees

| Attendee Problem | VenueAI Solution |
|---|---|
| "Where's the nearest food?" | Directs to closest stall with estimated wait time |
| "Gate is too crowded!" | Suggests 2 alternate crowd-free routes |
| "I need the restroom ASAP" | Points to nearest restroom and queue time |
| "Where do I park/exit?" | Provides smart parking exit guidance |
| "What's happening next?" | Shares event schedule updates |
| "I lost my bag!" | Guides to Lost & Found desk |
| "EMERGENCY!" | Provides immediate safety response protocol |

---

## How It Works (Step by Step)

1. Attendee opens **http://venue-link** on their phone browser
2. They type a question or tap a quick-action button
3. The question is sent to the Flask backend via a POST request
4. Flask passes the question + venue context to **Google Gemini API**
5. Gemini AI generates a concise, helpful response in seconds
6. The response is displayed in a clean chat bubble on the UI

---

## Google Gemini Integration Details

- **Package**: `google-genai` (official Google Gen AI Python SDK)
- **Model Used**: `gemini-2.0-flash-001` (with multi-model fallback chain)
- **Fallback Chain**: Automatically tries `gemini-2.0-flash`, `gemini-2.5-flash`, `gemini-2.5-flash-lite` if one is unavailable
- **System Prompt**: Venue-specific context injected into every query to keep responses relevant
- **API Key**: Loaded securely from `.env` using `python-dotenv`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + Flask |
| AI Engine | Google Gemini API (`google-genai`) |
| Frontend | Vanilla HTML/CSS/JavaScript |
| Config | `python-dotenv` (.env file) |

---

## Folder Structure

```
promptwars-venue-assistant/
├── app.py              # Flask backend with Gemini API integration
├── prompts.py          # AI system prompts
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .env                # API key (not committed to git)
└── templates/
    └── index.html      # Chat UI frontend
```

---

## How to Run Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/promptwars-venue-assistant
cd promptwars-venue-assistant/promptwars-venue-assistant
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set your Gemini API Key
Open `.env` and add your key:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
Get a free key at: https://aistudio.google.com/app/apikey

### Step 4: Run the app
```bash
python app.py
```

### Step 5: Open in browser
Navigate to: **http://127.0.0.1:5000**

---

## Google Services Used

- **Google Gemini API** — Natural language AI responses via `google-genai` SDK
- **Google AI Studio** — API key generation and model management

---

## Assumptions Made

- This is a prototype demonstrating AI capabilities. In production, it would connect to real-time venue sensor data for actual crowd densities and wait times.
- The assistant uses AI-generated estimates for wait times and routes based on general venue knowledge.
- Mobile-first design is critical since attendees access it via their smartphones during the event.
- The multi-model fallback chain ensures high availability during peak event times when AI servers may be under load.
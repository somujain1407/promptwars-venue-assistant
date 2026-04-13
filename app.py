from flask import Flask, request, jsonify, render_template
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SYSTEM_PROMPT = """You are VenueAI, a smart assistant 
for large-scale sporting venues. Help attendees with:
- Crowd navigation and shortest routes
- Food stall locations and wait times  
- Restroom locations and queue times
- Emergency assistance and safety
- Gate, entry and parking information
Be concise, helpful and friendly."""

# Model fallback list - tries each one until one works
MODEL_FALLBACKS = [
    "gemini-2.0-flash-001",
    "gemini-2.0-flash",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-flash-latest",
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            return jsonify({'response': 'API key missing in .env file'})

        client = genai.Client(api_key=api_key)
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nAssistant:"

        last_error = None
        for model in MODEL_FALLBACKS:
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=full_prompt
                )
                print(f"Success with model: {model}")
                return jsonify({'response': response.text})
            except Exception as e:
                error_msg = str(e)
                print(f"Model {model} failed: {error_msg[:100]}")
                last_error = error_msg
                # If quota exhausted for this model, try next one
                # If 503 overloaded, try next one
                continue

        # All models failed
        return jsonify({'response': f'All AI models are currently busy. Please try again in a moment. Last error: {last_error[:200]}'})

    except Exception as e:
        return jsonify({'response': f'Server error: {str(e)}'})

if __name__ == '__main__':
    print("VenueAI starting on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
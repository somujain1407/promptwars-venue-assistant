import os
from dotenv import load_dotenv

try:
    from google import genai
except ImportError:
    genai = None

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key and genai:
    client = genai.Client(api_key=api_key)
    try:
        models = client.models.list()
        print("Available models:")
        for m in models:
            print(m.name)
    except Exception as e:
        print("Error:", e)
else:
    print("API key missing or genai not installed")

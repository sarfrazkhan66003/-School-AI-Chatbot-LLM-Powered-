import os
from dotenv import load_dotenv

# ✅ Force load .env from project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

TEXT_DATA_DIR = os.path.join(BASE_DIR, "text_data")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 🔍 Debug print (temporary)
print("Loaded GROQ_API_KEY:", "FOUND" if GROQ_API_KEY else "NOT FOUND")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
LLM_MODEL = "llama3-8b-8192"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

FALLBACK_RESPONSE = (
    "Is sawal ki jankari hamare paas uplabdh nahi hai.\n"
    "Zyada jankari ke liye school se sampark kare.\n\n"
    "📞 Contact: +91-9876543210\n"
    "📧 Email: info@greenvalleyschool.edu"
)

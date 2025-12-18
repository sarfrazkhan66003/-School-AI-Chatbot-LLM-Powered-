import requests
from config import GROQ_API_URL, HEADERS, LLM_MODEL, FALLBACK_RESPONSE

PROMPT_TEMPLATE = """
You are a school information assistant.

Answer ONLY from the context.
If information is missing, say clearly "information not available".

Context:
{context}

Question:
{question}
"""

def ask_llm(context, question):
    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "user", "content": PROMPT_TEMPLATE.format(
                context=context,
                question=question
            )}
        ],
        "temperature": 0
    }

    try:
        response = requests.post(
            GROQ_API_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)   # 🔥 VERY IMPORTANT

        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print("❌ GROQ FAILED:", e)
        return FALLBACK_RESPONSE

import os
from dotenv import load_dotenv

load_dotenv()

USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "false").lower() == "true"

if not USE_MOCK_LLM:
    import openai
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(prompt: str) -> str:
    if USE_MOCK_LLM:
        print("🧪 MOCK MODE ENABLED — Prompt was:", prompt[:60])
        return f"🧪 MOCK RESPONSE: {prompt[:60]}..."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a Shopify logistics and ecommerce expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"OpenAI API error: {str(e)}"

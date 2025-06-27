# smoke_test.py
import os, openai, dotenv
dotenv.load_dotenv()             # pulls key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")
resp = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "ping"}]
)
print("LLM reply:", resp.choices[0].message.content)
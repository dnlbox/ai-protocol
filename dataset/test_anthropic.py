import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

try:
    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=10,
        messages=[{"role": "user", "content": "Hello"}]
    )
    print("SUCCESS: claude-3-5-haiku-20241022 works!")
except Exception as e:
    print(f"FAILED 3-5-haiku: {e}")

try:
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=10,
        messages=[{"role": "user", "content": "Hello"}]
    )
    print("SUCCESS: claude-haiku-4-5 works!")
except Exception as e:
    print(f"FAILED 4-5-haiku: {e}")

from dotenv import load_dotenv
import os

load_dotenv()


GROQ_API_KEY = os.getenv("GROK_API_KEY")

print(GROQ_API_KEY)

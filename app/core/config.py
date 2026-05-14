from dotenv import load_dotenv
import os

load_dotenv()


GROQ_API_KEY = os.getenv("GROK_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

from groq import Groq
from app.core.config import GROQ_API_KEY,MODEL_NAME

llm = Groq(api_key=GROQ_API_KEY)


def generate_response(promt: str):
    response = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": promt}],
        temperature=0,
        max_tokens=1024
    )

    return response.choices[0].message.content
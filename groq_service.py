import os
from dotenv import load_dotenv
from groq import Groq
from prompts import build_prompt

load_dotenv()


def generate_message(message, message_type, tone):
    """Send the user's request to Groq and return the generated text."""
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    model = os.getenv("GROQ_MODEL", "").strip()

    if not api_key or api_key == "your_groq_api_key_here":
        raise ValueError(
            "GROQ_API_KEY is missing. Add your Groq API key to the .env file."
        )
    if not model or model == "your_groq_model_id_here":
        raise ValueError(
            "GROQ_MODEL is missing. Add a currently supported Groq model ID to .env."
        )

    client = Groq(api_key=api_key)
    prompt = build_prompt(message, message_type, tone)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You write useful, respectful emails and messages.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    if not response.choices:
        raise RuntimeError("The AI returned an empty response.")
    return response.choices[0].message.content.strip()

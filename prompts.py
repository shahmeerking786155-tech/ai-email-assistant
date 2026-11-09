MESSAGE_TYPES = [
    "Professional Email",
    "Student Message",
    "Leave Application",
    "Formal Request",
]

TONES = [
    "Professional",
    "Polite",
    "Friendly",
]


def build_prompt(message, message_type, tone):
    """Create instructions for the AI using the selected type and tone."""
    return f"""
You are a helpful AI Email and Message Assistant.

Write a complete, clear, grammatically correct message using the details below.
Do not invent personal details, dates, names, or facts that were not provided.
If an important detail is missing, use a simple placeholder such as [Name] or [Date].

Message type: {message_type}
Tone: {tone}
User's details:
{message}

Return only the finished message. Do not add an explanation before or after it.
""".strip()

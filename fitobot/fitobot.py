# fitobot/fitobot.py
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY_HERE")  # Replace with your API key

def get_fitobot_response(user_input):
    """
    Takes user input, queries OpenAI, and returns Fitobot's reply.
    """
    if not user_input.strip():
        return "Please type something first!"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Fast and lightweight model
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Fitobot, a friendly AI fitness assistant. "
                    "Keep answers short, helpful, and motivating. "
                    "If the user mentions an exercise, give proper form tips."
                )
            },
            {"role": "user", "content": user_input}
        ]
    )

    return completion.choices[0].message.content

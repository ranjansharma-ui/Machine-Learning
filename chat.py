import os
from openai import OpenAI

# ✅ Your DeepSeek API key and endpoint
client = OpenAI(
    api_key="sk-56ac0a50fd4b4074abc09ea49aa41bb3",  # Replace this
    base_url="https://api.deepseek.com/v1"
)

print("Bot: Hello, how can I help you?\n")

messages = [
    {
        "role": "system",
        "content": "You are an expert at teaching science to kids. Your task is to engage in conversations about science and answer questions. Explain scientific concepts so they are easily understandable, use humor and analogies. Encourage curiosity.",
    }
]

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )
        reply = response.choices[0].message.content
        print(f"\nBot: {reply}\n")
        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print(f"\n[Error] {e}\n")

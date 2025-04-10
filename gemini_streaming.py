import os
from openai import OpenAI

token = os.environ["GOOGLE_API_KEY"]
endpoint = "https://generativelanguage.googleapis.com/v1beta/openai/"
model_name = "gemini-2.0-flash"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Initialize the conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    }
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Assistant: Goodbye!")
        break

    # Add the user's message to the conversation history
    messages.append({
        "role": "user",
        "content": user_input,
    })

    # Get the assistant's response
    response = client.chat.completions.create(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model_name
    )

    # Extract the assistant's reply
    assistant_reply = response.choices[0].message.content
    print(f"Assistant: {assistant_reply}")

    # Add the assistant's reply to the conversation history
    messages.append({
        "role": "assistant",
        "content": assistant_reply,
    })
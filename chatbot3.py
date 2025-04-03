import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Initialize the conversation history
messages = [
    SystemMessage("You are a helpful assistant."),
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Assistant: Goodbye!")
        break

    # Add the user's message to the conversation history
    messages.append(UserMessage(user_input))

    # Stream the assistant's response
    response = client.complete(
        stream=True,
        messages=messages,
        model_extras={'stream_options': {'include_usage': True}},
        model=model_name,
    )

    usage = {}
    assistant_reply = ""
    for update in response:
        if update.choices and update.choices[0].delta:
            delta_content = update.choices[0].delta.content or ""
            print(delta_content, end="")
            assistant_reply += delta_content
        if update.usage:
            usage = update.usage

    print("\n")  # Add a newline after the assistant's response

    # Add the assistant's reply to the conversation history
    messages.append(SystemMessage(assistant_reply))

    # Print usage statistics if available
    if usage:
        for k, v in usage.items():
            print(f"{k} = {v}")

client.close()
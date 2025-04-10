from openai import OpenAI

client = OpenAI(
    token = os.environ["GOOGLE_API_KEY"]
    endpoint = "https://generativelanguage.googleapis.com/v1beta/openai/"
    model_name = "gemini-2.0-flash"
    base_url= endpoint)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
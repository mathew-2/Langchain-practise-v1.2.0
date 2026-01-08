from openai import OpenAI

client = OpenAI(
    api_key="sk-h5jVFWHkWbYpJ8xIiEQz5g",  # Your provided API key
    base_url="http://3.110.18.218" # Your provided base URL
)

response = client.chat.completions.create(
    model="gemini-2.5-pro",  #Specify the model you want to use
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)

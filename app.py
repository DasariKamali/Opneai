from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="<OpenaiKey>",
    base_url="https://<OpenaiName>.openai.azure.com/openai", 
    api_version="2024-02-15-preview" 
)

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What can you do?"}
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city to get the weather for"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="computer-use-preview", 
    messages=chat_history,
    tools=tools,
    tool_choice="auto"
)

print(response.choices[0].message)

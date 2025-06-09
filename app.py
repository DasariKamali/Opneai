from openai import AzureOpenAI
import os
import logging

logging.basicConfig(level=logging.INFO)

config = {
    "api_key": "<OpenaiKey>",
    "endpoint": "https://<OpenaiName>.openai.azure.com/"
}

client = AzureOpenAI(
    api_key=config["api_key"],
    base_url=config["endpoint"],
    api_version="2025-04-01-preview"
)

parsed_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g., San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    }
]

chat_history = [
    {"role": "user", "content": "What’s the weather like in Mumbai in celsius?"}
]

response = client.responses.create(
    model="computer-use-preview",
    messages=chat_history,
    tools=parsed_tools,
    tool_choice="auto", 
    temperature=0.7,
    max_tokens=1024,
    truncation="auto"
)

print(response)

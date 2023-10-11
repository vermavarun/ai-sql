from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_type = os.getenv("OPEN_API_TYPE")
openai.api_base = os.getenv("OPEN_API_BASE")
openai.api_version = os.getenv("OPEN_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion_from_messages(system_message, user_message, model, temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]

    response = openai.ChatCompletion.create(
        engine=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message["content"]
from groq import Groq


def ask_llm(messages, api_key):

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    return response.choices[0].message.content
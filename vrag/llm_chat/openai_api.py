from openai import OpenAI  # openai==1.2.0


def chat_completions(api_key, base_url, model, messages):
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


client = OpenAI(
    api_key="up_Qt0FNm0YXZyHIXkUmfnVu6kEhFNWs",
    base_url="https://api.upstage.ai/v1/solar",
)

stream = client.chat.completions.create(
    model="solar-1-mini-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

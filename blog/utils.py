import openai

OPENAI_API_KEY="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"

openai.api_key = OPENAI_API_KEY

def generate_description(input):
    messages = [
        {"role": "user",
         "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply

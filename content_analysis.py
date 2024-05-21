import openai


# this function works, but it is not free to use openai api.
def text_analyzer(text):
    openai.api_key = "insert-openai-api-key"
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "/you are a text analyzer who is great at reading possible emotions from text. /Respond Yes "
                        "or No./"},
            {"role": "user",
             "content": "Does this text resemble something that may invoke an emotional response (this could be any "
                        "emotion including anger, happiness, inspiration, motivation, love, funny, joy, "
                        "etc.):" + text + "/Respond Yes. or No./"}
        ]
    )

    return completion.choices[0].message

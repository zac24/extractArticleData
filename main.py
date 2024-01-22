import openai
from secret_key import openai_key

client = openai
client.api_key = openai_key


def poem_on_samosa():
    prompt = 'write a poem for samosa, only 4 lines please.'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "write a poem for samosa, only 2 lines please"},
        ]
    )

    print(response.choices[0]['message']['content'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    poem_on_samosa()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

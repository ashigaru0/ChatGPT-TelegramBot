import openai

from sqlCommands.insertCommands import addDialog
from sqlCommands.selectCommands import getDialog

openai.api_key = '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'


async def makeRequest(text, chatName, userId):
    messages = getDialog(userId, chatName) + [{"role": "user", "content": text}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )['choices'][0]['message']

    messages.append({'role': response["role"], 'content': response["content"]})
    addDialog(userId, chatName, messages)

    return response['content']

from os import environ

import openai

from SQLCommands.insertCommands import addDialog
from SQLCommands.selectCommands import getDialog
from utils.checkTokens import checkTokensInMessage, checkTokensInDialog, clearDialog

openai.api_key = environ.get('OPENAI_API_KEY')


async def makeChatRequest(text, chatName, userId):
    if await checkTokensInMessage(text):
        return 'Вы привысили лимит токенов в сообщении.'

    if await checkTokensInDialog(await getDialog(userId, chatName)):
        await clearDialog(userId, chatName)
        return 'Вы привысили лимит токенов в диалоге.\n' \
               'Диалог был очищен.'

    messages = await getDialog(userId, chatName) + [{"role": "user", "content": text}]

    response = (await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=messages
    ))['choices'][0]['message']

    messages.append({'role': response["role"], 'content': response["content"]})
    await addDialog(userId, chatName, messages)

    return response['content']

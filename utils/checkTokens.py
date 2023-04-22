import tiktoken

from SQLCommands.insertCommands import addDialog


async def checkTokensInMessage(message):
    encoding = tiktoken.get_encoding('cl100k_base')
    tokens = len(encoding.encode(message))
    if tokens == 4067:
        return True
    return False


async def checkTokensInDialog(dialog):
    encoding = tiktoken.get_encoding('cl100k_base')
    tokens = 0
    for message in dialog:
        tokens += len(encoding.encode(message['content']))
    if tokens == 4067:
        return True
    return False


async def clearDialog(userId, chatName):
    await addDialog(userId, chatName, [])

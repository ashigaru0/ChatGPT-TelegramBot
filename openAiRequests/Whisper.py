from os import environ

import openai
import soundfile

openai.api_key = environ.get('OPENAI_API_KEY')


async def speechToText(fileId):
    data, samplerate = soundfile.read(f'temp/voice/ogg/{fileId}.ogg')
    soundfile.write(f'temp/voice/wav/{fileId}.wav', data, samplerate)

    audio_file = open(f'temp/voice/wav/{fileId}.wav', "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']

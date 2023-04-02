import openai
import soundfile

openai.api_key = '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'


async def speechToText(fileId):
    data, samplerate = soundfile.read(f'voice/ogg/{fileId}.ogg')
    soundfile.write(f'voice/wav/{fileId}.wav', data, samplerate)

    audio_file = open(f'voice/wav/{fileId}.wav', "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']

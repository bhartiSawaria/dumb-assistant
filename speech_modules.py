
from gtts import gTTS
from playsound import playsound
import os

def speak(value):
    tts = gTTS(str(value))
    tts.save('message.mp3')
    playsound('message.mp3')
    os.remove('message.mp3')

from assistant_details import getName
from speech_modules import speak
from database import getSpeakingStatus

def showOutput(out):
    name = getName()
    print(name + ": " + str(out))
    if getSpeakingStatus():
        speak(out)
    
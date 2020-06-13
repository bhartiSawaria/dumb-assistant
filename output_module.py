
from assistant_details import getName
from speech_modules import speak
from database import getSpeakingStatus
from internet import getInternetConnectionInfo

def showOutput(out):
    name = getName()
    print(name + ": " + str(out))
    if getSpeakingStatus() and getInternetConnectionInfo():
        speak(out)

    
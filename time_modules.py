
import datetime

def getDate():
    return str(datetime.date.today())

def getTime():
    currentTime = datetime.datetime.now()
    return str(currentTime.hour) + ":" + str(currentTime.minute)

def getHours():
    currentTime = datetime.datetime.now()
    return currentTime.hour


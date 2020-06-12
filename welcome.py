from time_modules import getDate, getHours
from database import getInfoFromInfoTable, updateInfoTable

def getGreetingMessage():
    currentDate = getDate()
    previousDate = getInfoFromInfoTable('previousDate')[0]

    if currentDate == previousDate:
        return "Welcome back!!"
    else:
        updateInfoTable('previousDate', currentDate)
        hour = getHours()
        if hour > 0 and hour < 12:
            return "Good morning!!"
        elif hour >= 12 and hour < 15:
            return "Good afternoon!!"
        else: 
            return "Good evening!!"
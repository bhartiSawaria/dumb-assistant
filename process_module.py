
from output_module import showOutput
from input_module import getInput
from database import getResultFromDatabase, insertIntoQueryAndResults, updateInfoTable, getSpeakingStatus
from time_modules import getDate, getTime
from internet import getInternetConnectionInfo, getAnsFromWikipedia
from assistant_details import getName, changeName
from speech_modules import speak
from toOpen_modules import openSomething, openGithub, playMusic
from weather_modules import getWeatherInfo
from news import getNewsHeadlines

def process(query):
    answer = getResultFromDatabase(query)

    if answer == 'startSpeaking':
        if getInternetConnectionInfo():
            speech = getSpeakingStatus()
            if speech:
                return 'I am already speaking'
            else:
                updateInfoTable('speech', 'on')
                return 'Okay I will speak now.'
        else:
            return 'Please turn on internet'

    elif answer == 'stopSpeaking':
        speech = getSpeakingStatus()
        if not speech:
            return 'I am not speaking'
        else:
            updateInfoTable('speech', 'off')
            return "Okay I won't speak now."

    elif answer == 'getTime':
        return getTime()

    elif answer == 'getDate':
        return getDate()

    elif answer == 'internetConnection':
        isConnected = getInternetConnectionInfo()
        if isConnected:
            return 'Your internet is connected'
        return 'Your internet is not connected'

    elif answer == 'playMusic':
        query = query.replace('play', '')
        return playMusic(query)

    elif answer == 'weatherConditions':
        if getInternetConnectionInfo():
            index = query.find('of')
            if index >= 0:
                index += 2
                query = query[index:]
                query = query.replace('city', '')
                query = query.strip()
                return getWeatherInfo(query)
            else:
                return "Sorry, I can't help with this one."
        else:
            return 'Your internet is not connected'

    elif answer == 'newsHeadlines':
        if getInternetConnectionInfo():
            return getNewsHeadlines()
        else:
            return 'Your internet is not connected'
    
    elif answer == 'open':
        if 'github' in query or  'account' in query:
            index = query.find('of')
            if index >= 0:
                index += 2
                toOpen = query[index:]
                toOpen = ((toOpen.replace(" ", "")).lower()).strip()
                return openGithub(toOpen)
            else:
                return "Sorry, I can't help with this one."
        else:
            index = query.find('open')
            if index >= 0:
                index += 4
                if index >= len(query):
                    return "Can't open, try another way."
                else:
                    toOpen = query[index:]
                    toOpen = ((toOpen.replace(" ", "")).lower()).strip()
                    return openSomething(toOpen)
            else:
                return "Sorry, I can't help with this one."

    elif answer == 'changeAssistantName':
        showOutput('Okay, what do you want to call me?')
        inp = input('User: ')
        if inp == getName():
            return 'It is my previous name.'
        else:
            changeName(inp)
            return 'Okay I change my name to ' + str(inp)
    
    else:
        showOutput("Don't know this one, should I search on internet?")
        inp = getInput()
        if "yes" in inp.lower():
            if getInternetConnectionInfo():
                return getAnsFromWikipedia(query)
            else:
                return "Your internet is not connected."
        else:
            showOutput("Then, can you please explain your question?")
            inp = getInput()
            if "yes" in inp.lower():
                showOutput("Please explain.")
                inp = getInput()
                ans = getResultFromDatabase(inp)
                if ans == "":
                    return "Sorry, I can't help with this one."
                else:
                    insertIntoQueryAndResults(query, ans)
                    return ans
            else:
                return "Sorry, I can't help with this one."


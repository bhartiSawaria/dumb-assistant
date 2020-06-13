
from output_module import showOutput
from input_module import getInput
from database import getResultFromDatabase, insertIntoQueryAndResults, updateInfoTable, getSpeakingStatus
from time_modules import getDate, getTime
from internet import getInternetConnectionInfo, getAnsFromWikipedia
from assistant_details import getName, changeName
from speech_modules import speak
from toOpen_modules import openSomething, openGithub, playMusic

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
        query =query.replace('play', '')
        return playMusic(query)
    
    elif answer == 'open':
        if 'github' in query or  'account' in query:
            index = query.find('of')
            index += 2
            toOpen = query[index:]
            toOpen = ((toOpen.replace(" ", "")).lower()).strip()
            return openGithub(toOpen)
        else:
            index = query.find('open')
            index += 4
            if index >= len(query):
                return "Can't open, try another way."
            else:
                toOpen = query[index:]
                toOpen = ((toOpen.replace(" ", "")).lower()).strip()
                return openSomething(toOpen)
    
    elif answer == 'gitHub':
        index = 0
        count = 0
        query = query.strip()
        for i in range(len(query), -1, -1):
            if query[i] == ' ':
                count += 1
            if count == 2:
                index = i
                break
        toOpen = query[index+1:]
        toOpen = ((toOpen.replace(" ", "")).lower()).strip()
        return openGithub(toOpen)

    elif answer == 'changeAssistantName':
        showOutput('Okay, what do you want to call me?')
        inp = input('User: ')
        if inp == getName():
            showOutput('It is my previous name.')
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


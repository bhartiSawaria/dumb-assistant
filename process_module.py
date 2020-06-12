
from output_module import showOutput
from input_module import getInput
from database import getResultFromDatabase, insertIntoQueryAndResults
from time_modules import getDate, getTime
from internet import getInternetConnectionInfo, getAnsFromWikipedia
from assistant_details import getName, changeName

def process(query):
    answer = getResultFromDatabase(query)
    if answer == 'getTime':
        return getTime()

    elif answer == 'getDate':
        return getDate()

    elif answer == 'internetConnection':
        isConnected = getInternetConnectionInfo()
        if isConnected:
            return 'Your internet is connected'
        return 'Your internet is not connected'

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


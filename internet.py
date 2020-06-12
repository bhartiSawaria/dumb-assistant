import wikipedia
import urllib.request

def getInternetConnectionInfo():
    try:
        urllib.request.urlopen('http://google.com') 
        return True
    except:
        return False

def getAnsFromWikipedia(que):
    try:
        data = wikipedia.summary(que, sentences=1)
        # print('Answer from wiki', data)
        return data
    except Exception as e:
        print('Answer from error wiki', e)
        return e


import wikipedia
import urllib.request
import webbrowser

def getInternetConnectionInfo():
    try:
        urllib.request.urlopen('http://google.com') 
        return True
    except:
        return False

def getAnsFromWikipedia(que):
    try:
        que = que.replace('what is', '')
        que = que.replace('who is', '')
        que = que.replace('tell me about', '')
        data = wikipedia.summary(que, sentences=1)
        return data
    except Exception as e:
        return "No results found."


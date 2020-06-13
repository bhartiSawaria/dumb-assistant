import webbrowser
from youtube_search import YoutubeSearch

def openSomething(name):
    webbrowser.open('https://' + name + '.com')
    return 'Opening ' + name

def openGithub(name):
    webbrowser.open('https://github.com/' + name )
    return 'Opening github account'

def playMusic(name):
    results = YoutubeSearch(name, max_results=10).to_dict()
    for i in results:
        webbrowser.open('https://youtube.com' + str(i['link']))
        return 'playing'
    
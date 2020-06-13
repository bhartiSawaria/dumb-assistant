import requests
from key_info import newsHeadlines

def getNewsHeadlines():
    answer = ''
    response = newsHeadlines()
    if response['status'] == 'ok':
        news = response['articles']
        for i in news:
            answer += i['title'] + ".\r\n"
        return answer
    else:
        return "Unable to get news from internet."



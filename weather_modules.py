
from time_modules import getDate
from key_info import city_forecast

def getWeatherInfo(query):
    result = city_forecast(query)
    answer = ''
    if result['cod'] == '404':
        return "Can't recognise this city."
    for i in result['list']:
        if i['dt_txt'][0:11].strip() == getDate().strip():
            if i['dt_txt'][11:13] == '03':
                answer += 'At 03:00 AM, ' + i['weather'][0]['description'] + ", "
            elif i['dt_txt'][11:13] == '06':
                answer += 'At 06:00 AM, ' + i['weather'][0]['description'] + ", "
            elif i['dt_txt'][11:13] == '09':
                answer += 'At 09:00 AM, ' + i['weather'][0]['description'] + ", "
            elif i['dt_txt'][11:13] == '12':
                answer += 'At 12:00 PM, ' + i['weather'][0]['description'] + ", "
            elif i['dt_txt'][11:13] == '15':
                answer += 'At 03:00 PM, ' + i['weather'][0]['description'] + ", "
            elif i['dt_txt'][11:13] == '18':
                answer += 'At 06:00 PM, ' + i['weather'][0]['description'] + ", "
            elif i['dt_txt'][11:13] == '21':
                answer += 'At 09:00 PM, ' + i['weather'][0]['description']
    
    return answer

    

    

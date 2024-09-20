'''
**Weather Data Retrieval:**
Write a program that fetches the current weather data for a specific city using a weather API.
- Utilize a weather API (such as OpenWeatherMap) to retrieve the current weather details (temperature, humidity, wind speed, etc.) for a user-input city.'''
import requests,json
class weather():
    def weather_details(self,a):
        api_key="9e760ead2c0f4e2af28f92e37c883338"
        url="https://api.openweathermap.org/data/2.5/weather?"
        update_url=url+"q="+a+"&appid="+api_key
        request=requests.get(update_url)
        if request.status_code==200:
            data=request.json()
            #emp_obj=json.load(request)
            #for emp in emp_obj['data'];
                #print(emp['temp'])
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            pressure=data['main']['pressure']
            description = data['weather'][0]['description']
            print(f"temperature:{temperature}")
            print(f"Humidity:{humidity}")
            print(f"pressure:{pressure}")
            print(f"description:{description}")
        else:
            print(f"request.status_code error")
input=input("Enter a city you want to get weather details:")
weather_api=weather()
weather_api.weather_details(input)

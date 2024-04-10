#Question 2

from weather_data import WeatherDataFetcher, DataParser
from user_interface import UserInterface

WDF = WeatherDataFetcher()
user = UserInterface()
while True:        
    try:   
        city = user.get_city()
        if city not in ['New York', 'London', 'Tokyo', 'Exit']:
            raise ValueError("Please pick a city between, 'New York', 'London', or 'Tokyo' ")
        if city == 'Exit':
            break
        temp, condition, humidity = WDF.weather_data[city].values()
        city_info = DataParser(city, temp, condition, humidity)

        if user.get_detail() == 'yes':
            city_info.get_city_info()
        else:
            print(city, WDF.weather_data[city])
    except Exception as e:
        print(e)




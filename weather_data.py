class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
    }
    # Logic for fetching weather data


class DataParser:
    def __init__(self, city, temperature, condition, humidity):
        self.city = city
        self.temperature= temperature
        self.condition= condition
        self.humidity=humidity

    # Logic for parsing weather data
    def get_city_info(self):
        print(f"Weather in {self.city}: {self.temperature} degrees, {self.condition}, Humidity: {self.humidity}%")
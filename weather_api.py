import requests

API_KEY = "14e86e65f07c6b4041b2327d267135e0"
city = "Delhi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

print(data)

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
weather = data["weather"][0]["description"]
city_name = data["name"]

print("City:", city_name)
print("Temperature:", temperature)
print("Humidity:", humidity)
print("Pressure:", pressure)
print("Weather:", weather)

from datetime import datetime
timestamp: datetime = datetime.now()
print("Timestamp:", timestamp)
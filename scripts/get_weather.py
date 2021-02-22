import requests, json

BASE = "https://api.openweathermap.org/data/2.5/weather?"
APIKEY = "fc2822e01a0efcce52cb56212fe44fd5"
CITY = "Stony Brook"
URL = BASE + "q="+ CITY + "&appid=" + APIKEY
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = main['temp'] #in Kelvin
    tempF = (temperature - 273.15) * (9/5) + 32
    humidity = main['humidity']
    pressure = main['pressure']
    report = data['weather']
    print("City: {}".format(CITY))
    print("Temperature (F): {}".format(tempF))
    print("Humidity: {}".format(humidity))
    print("Pressure: {}".format(pressure))
    print("Weather Report: {}".format(report[0]['description']))
else:
    print("Error in the HTTP Request")
    
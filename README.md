# WeatherAPI

Technical test for the Python Developer position at Globant.

This app is currently deployed at https://rocky-inlet-31249.herokuapp.com/weather :)

Request example:
```http
GET https://rocky-inlet-31249.herokuapp.com/weather?country=co&city=bogota
```

Response:
```json
{
  "location_name": "Bogotá, CO",
  "temperature": "14 °C",
  "wind": "Light breeze, 3.1 m/s, Northwest",
  "cloudines": "Scattered clouds",
  "presure": "1024 hPa",
  "humidity": "82%",
  "sunrise": "05:40",
  "sunset": "17:38",
  "geo_coordinates": "[4.61, -74.08]",
  "requested_time": "2020-10-30 01:22:09"
}
```

## Local use instructions

This instructions assume you are using bash, with python3, pip, and python3-venv installed.

Installation:
- Download the code
- Create virtual environment
- Install requirements
``` bash
git clone https://github.com/cazdlt/WeatherAPI.git
cd WeatherAPI
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Configuration:
- Done through environment variables
```bash
export OPEN_WEATHER_API_KEY="your_valid_open_weather_api_key"
export SECRET_KEY="replace_me"
```
Run the app:
```bash
flask run
```

## Requirement
<details>
  <summary>Original requirement</summary>
  
Goal:
>Create a Weather API using any framework you prefer.

General rules:
- Commit your changes frequently to a public repository in Github.
- Add a readme file with instructions to run the code

Support the following endpoints

```http
GET /weather?city=$City&country=$Country&
```
```json
{
    "location_name": "Bogota, CO",
    "temperature": "17 °C",
    "wind": "Gentle breeze, 3.6 m/s, west-northwest",
    "cloudines": "Scattered clouds", 
    "presure": "1027 hpa",
    "humidity": "63%",
    "sunrise": "06:07",
    "sunset": "18:00",
    "geo_coordinates": "[4.61, -74.08]",
    "requested_time": "2018-01-09 11:57:00"
}
```

- City is a string. Example: Medellín
- Country is a country code of two characters in - lowercase. Example: co
- This endpoint should use an external API to get the - proper info, here is an example: [OpenWeatherMap](http://api.openweathermap.org/data/2.5/weather?q=Bogota,co&appid=1508a9a4840a5574c822d70ca2132032)
- The data must be human-readable
- Use environment variables for configuration
- The response must include the content-type header - (application/json)
- Functions must be tested
- Keep a cache of 2 minutes of the data. You can use a persistent layer for this.
</details>



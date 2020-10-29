# WeatherAPI

Prueba técnica para el cargo de Python Developer en Globant

## Requerimiento

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

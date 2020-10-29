import datetime

import requests
from flask import Blueprint, current_app, request
from flask_restful import Api, Resource
from lxml import objectify

bp = Blueprint("api", __name__)
api = Api(bp)


def parse_weather_xml(xml: bytes) -> dict:

    weather = objectify.fromstring(xml)

    location_name = f"{weather['city'].attrib['name']}, {weather['city'].country}"

    temperature = weather["temperature"].attrib["value"] + " °C"

    wind_speed = weather["wind"]["speed"].attrib
    wind_dir = weather["wind"]["direction"].attrib
    wind = f"{wind_speed['name']}, {wind_speed['value']} {wind_speed['unit']}, {wind_dir.get('name','')}"

    # bad spelling but its the requirement
    cloudines = weather["clouds"].attrib["name"].capitalize()

    # bad spelling but its the requirement
    pressure_val = weather["pressure"].attrib
    presure = f"{pressure_val['value']} {pressure_val['unit']}"

    humidity_val = weather["humidity"].attrib
    humidity = f"{humidity_val['value']}{humidity_val['unit']}"

    # sunrise and sunset comes in GMT, timezone comes in "seconds shifted from GMT"
    sun = weather["city"]["sun"].attrib
    timezone_delta = datetime.timedelta(seconds=int(weather["city"]["timezone"]))
    date_format = r"%Y-%m-%dT%H:%M:%S"
    sunrise = datetime.datetime.strptime(sun["rise"], date_format) + timezone_delta
    sunset = datetime.datetime.strptime(sun["set"], date_format) + timezone_delta

    coords = weather["city"]["coord"].attrib
    geo_coordinates = f"[{coords['lat']}, {coords['lon']}]"

    requested_time = datetime.datetime.now()

    response = {
        "location_name": location_name,
        "temperature": temperature,
        "wind": wind,
        "cloudines": cloudines,  # bad spelling but following the requirement
        "presure": presure,  # bad spelling but following the requirement
        "humidity": humidity,
        "sunrise": sunrise.strftime(r"%H:%M"),
        "sunset": sunset.strftime(r"%H:%M"),
        "geo_coordinates": geo_coordinates,
        "requested_time": requested_time.strftime(r"%Y-%m-%d %H:%M:%S"),
    }

    return response


def get_weather(city: str, country_code: str) -> dict:

    url = "https://api.openweathermap.org/data/2.5/weather"

    apikey = current_app.config["OPEN_WEATHER_API_KEY"]
    remove_diacritics = lambda str: str.translate(
        str.maketrans(
            "áàäéèëíìïòóöùúüÀÁÄÈÉËÌÍÏÒÓÖÙÚÜ", "aaaeeeiiiooouuuAAAEEEIIIOOOUUU"
        )
    )

    params = {
        "q": f"{remove_diacritics(city)},{country_code}",
        "appid": apikey,
        "units": "metric",
        "mode": "xml",
        "lang": "en",
    }

    response = requests.get(url, params=params)

    if response.status_code == 401:
        # wrong api key
        error = response.json()
        return {"error": {"code": int(error["cod"]), "message": str(error["message"])}}

    elif response.status_code != 200:
        # other errors should send XML
        error = objectify.fromstring(response.content)
        return {"error": {"code": int(error.cod), "message": str(error.message)}}

    return parse_weather_xml(response.content)


class Weather(Resource):
    def get(self):
        # query params
        city = request.args.get("city")
        country = request.args.get("country")

        if not city or not country:
            error = {
                "error": {
                    "code": 400,
                    "message": "Both city and country must be specified",
                }
            }
            return error, 400

        weather = get_weather(city, country)

        if "error" in weather:
            return weather, weather["error"]["code"]

        return weather, 200


api.add_resource(Weather, "/weather")

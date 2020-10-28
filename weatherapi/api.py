from flask import Blueprint, current_app
from flask_restful import Api, Resource
import requests

bp = Blueprint("api", __name__)
api = Api(bp)


def get_weather(city: str, country_code: str) -> dict:

    url = "https://api.openweathermap.org/data/2.5/weather"

    apikey = current_app.config["OPEN_WEATHER_API_KEY"]
    remove_diacritics = lambda str: str.translate(
        str.maketrans(
            "áàäéèëíìïòóöùúüÀÁÄÈÉËÌÍÏÒÓÖÙÚÜ", "aaaeeeiiiooouuuAAAEEEIIIOOOUUU"
        )
    )

    params = {"q": f"{remove_diacritics(city)},{country_code}", "appid": apikey}
    response = requests.get(url, params=params)

    return response.json()


class Weather(Resource):
    def get(self):
        # todo
        pass


api.add_resource(Weather, "/weather")

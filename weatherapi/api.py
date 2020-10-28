from flask_restful import Api, Resource
from flask import Blueprint

bp = Blueprint("api", __name__)
api = Api(bp)


def get_weather(city: str, country_code: str) -> dict:
    # todo request data from openweather api
    pass


class Weather(Resource):
    def get(self):
        # todo
        pass


api.add_resource(Weather, "/weather")

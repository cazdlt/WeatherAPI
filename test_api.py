import time

import pytest

from weatherapi import create_app
from weatherapi.api import get_weather


@pytest.fixture(scope="session")
def app():
    app = create_app(dev=True)
    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        yield client


def test_openweather(app):
    # Test the OpenWeather API

    # normal
    weather = get_weather("Bogota", "CO")
    assert "location_name" in weather
    assert "temperature" in weather
    assert "wind" in weather
    assert "cloudines" in weather
    assert "presure" in weather
    assert "humidity" in weather
    assert "sunrise" in weather
    assert "sunset" in weather
    assert "geo_coordinates" in weather
    assert "requested_time" in weather
    assert weather["geo_coordinates"] == "[4.61, -74.08]"

    # with accent
    weather = get_weather("Bogotá", "CO")
    assert "location_name" in weather
    assert "temperature" in weather
    assert "wind" in weather
    assert "cloudines" in weather
    assert "presure" in weather
    assert "humidity" in weather
    assert "sunrise" in weather
    assert "sunset" in weather
    assert "geo_coordinates" in weather
    assert "requested_time" in weather
    assert weather["geo_coordinates"] == "[4.61, -74.08]"

    # city does not exist
    weather = get_weather("Bogotá", "FR")
    assert "error" in weather
    assert weather["error"]["code"] == 404
    assert weather["error"]["message"] == "city not found"


@pytest.mark.parametrize(
    "city,country",
    [
        ("Bogota", "CO"),
        ("Bogotá", "CO"),
        ("Medellín", "co"),
        ("Paris", "fr"),
        ("Windhoek", "Na"),
        ("seoul", "kr"),
        ("barrancabermeja", "co"),
    ],
)
def test_api(client, city, country):
    url = "/weather"

    params = {
        "city": city,
        "country": country,
    }
    response = client.get(url, query_string=params)
    weather = response.json

    assert response.headers["Content-Type"] == "application/json"
    assert "location_name" in weather
    assert "temperature" in weather
    assert "wind" in weather
    assert "cloudines" in weather
    assert "presure" in weather
    assert "humidity" in weather
    assert "sunrise" in weather
    assert "sunset" in weather
    assert "geo_coordinates" in weather
    assert "requested_time" in weather


@pytest.mark.parametrize(
    "city,country,error_code",
    [
        ("Botota", "CO", 404),
        ("Cali", "uk", 404),
        (None, None, 400),
        ("Buenaventura", "", 400),
        ("", "jp", 400),
        ("kinshasa", None, 400),
    ],
)
def test_api_bad_input(client, city, country, error_code):
    url = "/weather"

    params = {
        "city": city,
        "country": country,
    }
    response = client.get(url, query_string=params)
    weather = response.json

    assert response.headers["Content-Type"] == "application/json"
    assert "error" in weather
    assert error_code == weather["error"]["code"]


def test_cache(client):
    # tested manually

    url = "/weather"
    params = {
        "city": "Cali",
        "country": "co",
    }
    time.sleep(120)
    response = client.get(url, query_string=params)
    response2 = client.get(url, query_string=params)

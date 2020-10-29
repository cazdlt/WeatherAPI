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

    # city does not exist
    weather = get_weather("Bogotá", "FR")
    assert "error" in weather
    assert weather["error"]["code"] == 404
    assert weather["error"]["message"] == "city not found"


def test_api():
    # todo basic test of my api fields and headers
    pass


def test_api_bad_input():
    # todo basic test of my api fields and headers
    pass


def test_cache():
    # todo test two hour caching (can be done?)
    pass

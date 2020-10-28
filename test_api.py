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

    # ok
    weather = get_weather("Bogota", "CO")
    assert weather["coord"]["lat"] == 4.61
    assert weather["coord"]["lon"] == -74.08
    assert weather["name"] == "Bogotá"

    # con tilde
    weather = get_weather("Bogotá", "CO")
    assert weather["coord"]["lat"] == 4.61
    assert weather["coord"]["lon"] == -74.08
    assert weather["name"] == "Bogotá"

    # ciudad no existe
    weather = get_weather("Bogotá", "FR")
    assert weather["message"] == "city not found"


def test_api():
    # todo basic test of my api fields and headers
    pass


def test_api_bad_input():
    # todo basic test of my api fields and headers
    pass


def test_cache():
    # todo test two hour caching (can be done?)
    pass

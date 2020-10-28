import pytest

from weatherapi import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app(dev=True)
    yield app


def test_openweather():
    # todo test the openweather api
    pass


def test_api():
    # todo basic test of my api fields and headers
    pass


def test_cache():
    # todo test two hour caching (can be done?)
    pass

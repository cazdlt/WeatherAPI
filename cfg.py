import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
    OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
    CACHE_TYPE = "filesystem"  # persistent layer (can also be Redis)
    CACHE_DEFAULT_TIMEOUT = 120
    CACHE_DIR = ".cache/"
    ENV = "development"


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
    CACHE_TYPE = "filesystem"  # persistent layer (can also be Redis)
    CACHE_DEFAULT_TIMEOUT = 120
    CACHE_DIR = ".cache/"
    ENV = "production"

from flask import Flask
from flask_caching import Cache
import cfg

cache = Cache()


def create_app(dev=False) -> Flask:

    app = Flask(__name__)

    if dev:
        app.config.from_object(cfg.DevConfig)
    else:
        app.config.from_object(cfg.Config)

    cache.init_app(app)

    from .api import bp as api

    app.register_blueprint(api)

    return app

from flask import Flask
import cfg


def create_app(dev=False) -> Flask:

    app = Flask(__name__)

    if dev:
        app.config.from_object(cfg.DevConfig)
    else:
        app.config.from_object(cfg.Config)

    from .api import bp as api

    app.register_blueprint(api)

    return app

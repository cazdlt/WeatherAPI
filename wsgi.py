from weatherapi import create_app
import os

dev = os.environ.get("FLASK_ENV") == "development"
app = create_app(dev)

if __name__ == "__main__":
    app.run()

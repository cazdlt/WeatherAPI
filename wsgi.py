from weatherapi import create_app
import os

dev = os.environ.get("ENV") == "dev"
app = create_app(dev)

if __name__ == "__main__":
    app.run()

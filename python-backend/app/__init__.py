from flask import Flask
from app.routes import app as routes_app

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Load configuration
    app.register_blueprint(routes_app)  # Register the routes blueprint
    return app

app = create_app()

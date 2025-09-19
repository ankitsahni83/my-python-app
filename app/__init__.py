from flask import Flask
from app.routes.hello import hello_bp
from app.errors import register_error_handlers
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    errors.register_error_handlers(app)
    app.register_blueprint(hello_bp)

    return app
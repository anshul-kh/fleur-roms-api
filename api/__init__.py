from flask import Flask
from api.routes.roms import roms
from api.routes.recovery import recovery


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(roms)
    app.register_blueprint(recovery)
    
    return app
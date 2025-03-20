from flask import Flask
from .config import Config
from .extensions import login_manager, db, bcrypt
from . import auth, habit

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth.bp, url_prefix = "/auth")
    app.register_blueprint(habit.bp)

    return app


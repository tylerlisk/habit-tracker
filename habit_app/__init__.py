from flask import Flask
from .config import Config
from .extensions import login_manager, db, bcrypt
from . import auth, habit
import os

def create_app():
    app = Flask(__name__)
    
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    INSTANCE_DIR = os.path.join(BASE_DIR, "..", "instance") 
    os.makedirs(INSTANCE_DIR, exist_ok=True)
     
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(INSTANCE_DIR, 'habit_database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth.bp, url_prefix = "/auth")
    app.register_blueprint(habit.bp)


    with app.app_context():
        from . import models
        db.create_all()

    return app


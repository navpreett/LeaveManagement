from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)  # Use Config class for configuration

db = SQLAlchemy(app)
login_manager = LoginManager(app)  # Initialize LoginManager after creating the app instance

from app import routes, models

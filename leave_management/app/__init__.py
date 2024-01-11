# app/__init__.py
from flask import Flask
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app instance
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# Initialize the SQLAlchemy instance without passing the app instance
db = SQLAlchemy()

# Initialize the app with the SQLAlchemy instance
db.init_app(app)


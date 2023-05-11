from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rocks.db'
app.config ['SECRET_KEY'] = 'iloveemobitches'
db = SQLAlchemy(app)

from app import routes, models, forms

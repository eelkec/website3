from app import app
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import render_template, redirect

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

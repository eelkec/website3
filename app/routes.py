from app import app, db
from app.models import Boulder,User
from app.forms import MyForm
from flask import render_template, redirect, request, url_for
from flask_login import LoginManager
login_manager = LoginManager()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('rocks.html', users=users)
    results = query_db ('SELECT * FROM name')

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('rocks'))

@app.route('/add', methods=['GET','POST'])
def add_boulder():
    if request.method == 'POST':
        image = request.form['image']
        name = request.form['name']
        description = request.form['description']
        grade = request.form['grade']

        boulder = Boulder(boulder=boulder, image=image, description=description, grade=grade, name=name)

        db.session.add(boulder)
        db.session.commit()
        return redirect(url_for('rocks'))
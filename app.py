from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

DATABASE = "database.db"

def query_db(sql,args=(),one=False):
    '''connect and query- will retun one item if one=true and can accept arguments as tuple'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute(sql, args)
    results = cursor.fetchall()
    db.commit()
    db.close()
    #return None if ther is no result from the query
    #return the first item only if one=True
    #return the list of tuples if one=False
    return (results[0] if results else None) if one else results

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __repr__(self):
        return '<User %r>' % self.name
    
class Boulder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, foreign_key=True)
    name = db.Column(db.String(120))
    image = db.Column(db.String(80))
    grade = db.Column(db.String(50))
    description = db.Column(db.String(120))

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

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

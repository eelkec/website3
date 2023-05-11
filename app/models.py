#this will be my data models
from app import db

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
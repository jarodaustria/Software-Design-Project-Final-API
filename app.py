from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'group48'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Trainee(db.Model):
    __tablename__ = 'trainee'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    age = db.Column(db.Integer)
    registered_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'password': self.password,
            'age': self.age
        }
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
class Trainer(db.Model):
    __tablename__ = 'trainer'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    age = db.Column(db.Integer)
    registered_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'password': self.password,
            'age': self.age
        }
    
@app.route('/trainees', )
def all_trainees():
    trainees = Trainee.query.all()
    return jsonify(trainees = [item.serialize for item in trainees])

@app.route('/trainers')
def all_trainers():
    trainers = Trainer.query.all()
    return jsonify(trainers = [item.serialize for item in trainers])

@app.route('/courses')
def all_courses():
    courses = Course.query.all()
    return jsonify(courses = [item.serialize for item in courses])

@app.route('/test')
def test():
    return 'test'


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=8080, debug=True)
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
    @property
    def serialize_email_password(self):
        return {
            'email': self.email,
            'password': self.password,
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
    @property
    def serialize_email_password(self):
        return {
            'email': self.email,
            'password': self.password,
        }
    
@app.route('/trainees')
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

@app.route('/trainee/signup', methods=['POST'])
def trainee_signup():
    request_data = request.get_json()

    new_trainee = Trainee(full_name = request_data['full_name'],
                        email = request_data['email'],
                        password = request_data['password'],
                        age = request_data['age'])
    db.session.add(new_trainee)
    db.session.commit()
    return 'trainee added successfully'

@app.route('/trainee/email=<string:email>')
def trainee_by_email(email):
    trainee = Trainee.query.filter_by(email=email).first()
    return jsonify(trainee.serialize_email_password)

@app.route('/trainer/signup', methods=['POST'])
def trainer_signup():
    request_data = request.get_json()

    new_trainer = Trainer(full_name = request_data['full_name'],
                        email = request_data['email'],
                        password = request_data['password'],
                        age = request_data['age'])
    db.session.add(new_trainer)
    db.session.commit()
    return 'trainer successfully added'

@app.route('/test')
def test():
    return 'test'


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=8080, debug=True)
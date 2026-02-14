from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    finished_works = db.relationship('FinishedWork', backref='employee', cascade='all, delete-orphan')

class FinishedWork(db.Model):
    __tablename__ = 'finished_work'
    id = db.Column(db.Integer, primary_key=True)
    work = db.Column(db.String(100), nullable=False)
    estimate = db.Column(db.Float, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
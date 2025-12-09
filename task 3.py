from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.sql.ddl import CreateTable

# Configuration
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)

    # Relation with FinishedWork (one project has many FinishedWork
    to_finish_the_work = db.relationship('Finished Work', backref='project', cascade='all, delete-orphan')

class FinishedWork(db.Model):
    __tablename__ = 'finished_work'
    id = db.Column(db.Integer, primary_key=True)
    work = db.Column(db.String(100), nullable=False)
    estimate = db.Column(db.Float, nullable=False)
    company = db.Column(db.String(100), nullable=False)





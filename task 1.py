from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myprojects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'::Title {self.title}, price: {self.price}, creation_date: {self.creation_date}::'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_projects = Project.query.all()
    return render_template('index.html', my_projects=all_projects)

if __name__ == '__main__':
    app.run()





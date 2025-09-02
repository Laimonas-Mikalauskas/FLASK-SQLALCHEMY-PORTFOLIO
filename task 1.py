from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manoprojektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Projektas(db.Model):
    __tablename__ = 'projektai'

    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String(200), nullable=False)
    kaina = db.Column(db.Float, nullable=False)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'::Pavadinimas {self.pavadinimas}, kaina: {self.kaina}, sukurimo data: {self.sukurimo_data}::'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_projects = Projektas.query.all()
    return render_template('index.html', my_projects=all_projects)

if __name__ == '__main__':
    app.run()





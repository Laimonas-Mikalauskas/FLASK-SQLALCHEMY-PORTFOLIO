from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)


class Projektas(db.Model):
    __tablename__ = 'projektas'

    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String(100), nullable=False)
    kaina = db.Column(db.Float, nullable=False)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"<Projektas {self.pavadinimas}, {self.kaina} EUR>"


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    projektai = Projektas.query.all()
    return render_template('index.html', projektas_rows=projektai)


if __name__ == '__main__':
    app.run()



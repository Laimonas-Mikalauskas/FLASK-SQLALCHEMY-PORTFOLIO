import cur
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

from sqlalchemy import sql
from sqlalchemy.orm import with_parent
from sqlalchemy.sql.ddl import CreateTable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

cur.execute("""
CreateTable with SQLAlchemy "Projects" (
            project id: "0000",
            project name: "Python",
            price: "1000$",
            creation date: "2025/07/10"
            actions: "Edit"; "Delete";
    
)
""")

if __name__ == '__main__':
    app.run()





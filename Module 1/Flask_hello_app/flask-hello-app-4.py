# Creating tables from db.Model(person class)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://saadshamim@localhost:5432/fullstack'

#Instance of database
db = SQLAlchemy(app)

class Person(db.Model):

    #Name of the table
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)

db.create_all()

@app.route('/')

def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

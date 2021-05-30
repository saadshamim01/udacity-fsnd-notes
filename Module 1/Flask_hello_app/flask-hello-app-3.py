# Creating db.Model and defining models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://saadshamim@localhost:5432/fullstack'

#Instance of database
db = SQLAlchemy(app)

#db.Model: Creating and manipulating data models
#db.session: Creating and manipulating database transactions

#Creating person class

class Person(db.Model):

    #Name of the table
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)


@app.route('/')

def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run()


#To run the script in debug mode (in terminal)
#FLASK_APP=app.py FLASK_DEBUG=true flask run
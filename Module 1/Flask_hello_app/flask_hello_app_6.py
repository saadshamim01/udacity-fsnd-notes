#Changing the name of the file to import it using python

# class User(db.Model):
#   ...
#   name = db.Column(db.String(), nullable=False, unique=True

#Checking constrains using db.CheckConstraint

# class Product(db.Model):
#   ...
#   price = db.Column(db.Float, db.CheckConstraint('price>0'))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://saadshamim@localhost:5432/fullstack'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Person(db.Model):

    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)

#To customise the output return string
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

@app.route('/')

def index():

    #Returning a query
    person = Person.query.first()
    return 'Hello ' + person.name

if __name__ == '__main__':
    app.run()
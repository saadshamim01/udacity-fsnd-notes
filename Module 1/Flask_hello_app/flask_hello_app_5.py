#Inserting Records and Using Debug Mode

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://saadshamim@localhost:5432/fullstack'

#Prevents error
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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

    #Returning a query
    person = Person.query.first()
    return 'Hello ' + person.name

if __name__ == '__main__':
    app.run()

#If changes made to file, reloading updates the page
# FLASK_APP=flask-hello-app-5.py FLASK_DEBUG=true flask run

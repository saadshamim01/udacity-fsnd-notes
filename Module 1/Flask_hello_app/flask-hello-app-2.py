# Creating Hello App with Flask-SQLALchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Connecting to database, setting configuration variable
#DIALECT USERNAME PASSWORD HOST PORT DBNAME
#'postgresql://myusername:mypassword@localhost:5432/mydatabase'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://saadshamim@localhost:5432/fullstack'


#To link database with flask app
db = SQLAlchemy(app)


@app.route('/')

def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run()


#To run the script in debug mode (in terminal)
#FLASK_APP=app.py FLASK_DEBUG=true flask run
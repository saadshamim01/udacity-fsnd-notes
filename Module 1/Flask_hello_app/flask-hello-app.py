#Basic Flask app

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello World'

#Additional functionality to not write
#FLASK_APP = flask-hello-app.py flask run

if __name__ == '__main__':
    app.run()


#To run the script in debug mode (in terminal)
#FLASK_APP=app.py FLASK_DEBUG=true flask run
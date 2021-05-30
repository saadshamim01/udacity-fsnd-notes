from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #Rendering a template instead of hello world
    return render_template('index.html', data=[

                    {'description': 'Todo1'},

                    {'description' : 'Todo2'},

                    {'description' : 'Todo3'}

                    ])
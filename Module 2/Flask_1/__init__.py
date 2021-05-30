from flask import Flask, jsonify
from models import setup_db, Plant

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    @app.route('/')
    def hello():
        return jsonify({'message': 'HELLO WORLD'})





    return app
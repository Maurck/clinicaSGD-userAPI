'''
config.py: modulo donde se configura la aplicación
'''
import os
from dotenv import load_dotenv
from flask import Flask
from flask_lambda import FlaskLambda
from flask_cors import CORS

def server_config(app):
    load_dotenv()
    cors_config(app)


def cors_config(app):
    CORS(app=app, supports_credentials=True)

def get_app(__name__):

    server_status = os.getenv('SERVER_STATUS', 'DEVELOPMENT')

    if server_status == 'DEVELOPMENT':
        app = Flask(__name__)
    elif server_status == 'PRODUCTION':
        app = FlaskLambda(__name__)

    return app

def run_app(app):
    server_status = os.getenv('SERVER_STATUS', 'DEVELOPMENT')

    if server_status == 'DEVELOPMENT':
        app.run(debug=True, host='0.0.0.0', port=5000)
    elif server_status == 'PRODUCTION':
        app.run(debug=True)
    

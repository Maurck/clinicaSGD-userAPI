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
    app_cofig(app)

def app_cofig(app):
    app.secret_key = os.getenv('SECRET_KEY')

    server_status = os.getenv('SERVER_STATUS', 'DEVELOPMENT')

    if server_status == 'DEVELOPMENT':
        app.config.update(
            SERVER_NAME=os.getenv('DEVELOPMENT_SERVER_NAME'),
            SESSION_COOKIE_NAME=os.getenv('DEVELOPMENT_SERVER_NAME'),
            SESSION_COOKIE_DOMAIN=os.getenv('DEVELOPMENT_SERVER_NAME'),
        )
    elif server_status == 'PRODUCTION':
        app.config.update(
            SERVER_NAME=os.getenv('PRODUCTION_SERVER_NAME'),
            SESSION_COOKIE_NAME=os.getenv('PRODUCTION_SERVER_NAME'),
            SESSION_COOKIE_DOMAIN=os.getenv('PRODUCTION_SERVER_NAME')
        )


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
    

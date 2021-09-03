'''
utils.py: Modulo para definir los metodos de funcionalidad auxiliar
'''
import requests
from requests.auth import HTTPBasicAuth
import os
from flask import jsonify
from cerberus import Validator


def json_message(msg):
    '''
    Metodo que devuelve un mensaje en formato json
    '''
    return jsonify({
        "message": msg
    })

def validate_parameters(parameters, schema):
    v = Validator(schema)
    v.allow_unknown = True
    if not v.validate(parameters):
        return jsonify({
            "errors": v.errors
        })

def get_csrf_token(user_name, user_password):
    #Obtener CSRFToken
    mayan_root_url = os.getenv('MAYAN_ROOT_URL')
    mayan_admin_user = os.getenv('MAYAN_ADMIN_USER')
    mayan_admin_password = os.getenv('MAYAN_ADMIN_PASSWORD')

    url_token = "{}/api/v4/auth/token/obtain/".format(mayan_root_url)
    payload_token_mayan = {'username':user_name, 'password':user_password}
    r_token = requests.get(url_token, auth=HTTPBasicAuth(mayan_admin_user, mayan_admin_password), data=payload_token_mayan)
    
    return r_token.cookies.get('csrftoken')
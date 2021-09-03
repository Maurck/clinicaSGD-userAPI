'''
register.py: Modulo para el registro
'''
import requests
from requests.auth import HTTPBasicAuth
import os


class RegisterFlow:
    '''
    Clase que registra a un usuario
    '''
    def __call__(self, request):

        # Obtener email y contraseña

        req_user_name = request.form['user_name']
        req_user_password = request.form['user_password']

        # Conectar con la API user de Manyan
        mayan_root_url = os.getenv('MAYAN_ROOT_URL')
        mayan_admin_user = os.getenv('MAYAN_ADMIN_USER')
        mayan_admin_password = os.getenv('MAYAN_ADMIN_PASSWORD')

        url_create_user_mayan = "{}/api/v4/users/".format(mayan_root_url)
        payload_create_user_mayan = {'username':req_user_name, 'password':req_user_password}
        r_create = requests.post(url_create_user_mayan, data = payload_create_user_mayan, auth=HTTPBasicAuth(mayan_admin_user, mayan_admin_password))

        # Hacer administrador de mayan       
        url_make_admin_mayan = "{}/api/v4/groups/2/users/add/".format(mayan_root_url)
        user_id_mayan = r_create.json()["id"]    
        payload_make_admin_mayan = {'user': user_id_mayan}
        r_make_admin = requests.post(url_make_admin_mayan, data = payload_make_admin_mayan, auth=HTTPBasicAuth(mayan_admin_user, mayan_admin_password))

        return r_create.json()

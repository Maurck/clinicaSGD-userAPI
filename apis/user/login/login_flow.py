import requests
from flask import jsonify
from requests.auth import HTTPBasicAuth
from utils.utils import get_csrf_token
import os


class LoginFlow:

    def __call__(self, request):

        # Obtener email y contraseña
        req_user_name = request.form['user_name']
        req_user_password = request.form['user_password']

        mayan_root_url = os.getenv('MAYAN_ROOT_URL')
        mayan_admin_user = os.getenv('MAYAN_ADMIN_USER')
        mayan_admin_password = os.getenv('MAYAN_ADMIN_PASSWORD')

        csrf_token = get_csrf_token(req_user_name, req_user_password)
        print("primera token creada: " + csrf_token)

        #Logout
        url_logout_mayan = "{}/authentication/logout/".format(mayan_root_url)
        # payload_logout_mayan = {'username':req_user_name, 'password':req_user_password}
        logout_headers = {'X-CSRFTOKEN': csrf_token, 'Cookie': 'csrftoken={}'.format(csrf_token)}
        r_logout = requests.post(url_logout_mayan, auth=HTTPBasicAuth(mayan_admin_user, mayan_admin_password), headers=logout_headers)
        print("usuario deslogueado")

        return jsonify(r_logout.text)
        
        # Login
        url_login_mayan = "{}/authentication/login/?next=/api/v4/users/current/".format(mayan_root_url)
        payload_login_mayan = {'username':req_user_name, 'password':req_user_password}
        login_headers = {'X-CSRFTOKEN': csrf_token}
        r_create = requests.post(url_login_mayan, data = payload_login_mayan, auth=HTTPBasicAuth(mayan_admin_user, mayan_admin_password), headers=login_headers)

        print("nuevo usuario logueado")
        return jsonify(r_create.text)





'''
user.py: Modulo para definir las rutas relacionadas con la API User
'''
from flask import request
from apis.user.register.register import Register


def create_routes_user(app):
    '''
    Metodo que crea las rutas relacionadas con la API User
    '''

    @app.route('/register', methods=['POST'])
    def register():
        register = Register()
        return register(request)


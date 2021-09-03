from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models.user import User
from utils.utils import json_message


class GetUserFlow:
    def __call__(self, request):

        user_id = request.args.get('user_id')

        if user_id is not None:
            user_obj = User.objects(
                id=user_id
            ).first()

            if user_obj is not None:
                return jsonify({"user": user_obj.to_json()})

            return json_message("Usuario no encontrado")

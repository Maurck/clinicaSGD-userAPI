from utils.utils import validate_parameters

login_body_schema = {
    'user_name': {
        'nullable': False,
        'required': True
    },
    'user_password': {
        'nullable': False,
        'required': True
    } 
}

class LoginValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.form, login_body_schema)
        return body_validation_errors
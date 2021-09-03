from .login_validator import LoginValidator
from .login_flow import LoginFlow


class Login:

    def __call__(self, request):

        login_validation = LoginValidator()
        login_validation_errors = login_validation(request)
        if login_validation_errors:
            return login_validation_errors

        login_flow = LoginFlow()
        return login_flow(request) 

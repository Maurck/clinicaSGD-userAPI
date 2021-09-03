from .get_user_validator import GetUserValidator
from .get_user_flow import GetUserFlow


class GetUser:

    def __call__(self, request):

        get_user_validation = GetUserValidator()
        get_user_validation_errors = get_user_validation(request)
        if get_user_validation_errors:
            return get_user_validation_errors

        get_user_flow = GetUserFlow()
        return get_user_flow(request)

            

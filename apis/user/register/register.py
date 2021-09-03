from .register_validator import RegisterValidator
from .register_flow import RegisterFlow


class Register:

    def __call__(self, request):

        register_validation = RegisterValidator()
        register_validation_errors = register_validation(request)
        if register_validation_errors:
            return register_validation_errors

        register_flow = RegisterFlow()
        return register_flow(request)

            

from utils.utils import validate_parameters

get_user_query_schema = {
    'user_id': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 24,
        'maxlength': 24
    }
}

class GetUserValidator:
    
    def __call__(self, request):
        query_validation_errors = validate_parameters(request.args, get_user_query_schema)
        return query_validation_errors
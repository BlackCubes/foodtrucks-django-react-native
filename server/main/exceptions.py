from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    handlers = {
        'ValidationError': _handle_validation_error,
        'Http404': _handle_generic_error,
        'NotFound': _handle_generic_error,
        'MethodNotAllowed': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'ParseError': _handle_generic_error,
        'UnsupportedMediaType': _handle_generic_error,
        'AuthenticationFailed': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
    }

    response = exception_handler(exc, context)

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def _handle_authentication_error(exc, context, response):
    response.data = {
        'statusCode': response.status_code,
        'status': 'fail',
        'message': 'Please login to continue.',
    }

    return response


def _handle_generic_error(exc, context, response):
    response.data = {
        'statusCode': response.status_code,
        'status': 'fail',
        'message': response.data['detail'],
    }

    return response


def _handle_validation_error(exc, context, response):
    response.data = {
        'statusCode': response.status_code,
        'status': 'fail',
        'message': 'Validation errors in your request.',
        'errors': response.data,
    }

    return response

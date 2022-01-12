from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    handlers = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
    }

    response = exception_handler(exc, context)
    print(exc)

    if response is not None:
        custom_response = {}

        custom_response['statusCode'] = response.status_code
        custom_response['status'] = 'fail'

        condense_messages = []

        for value in response.data.values():
            if not isinstance(value, str):
                condense_messages.append(' '.join(value))
            else:
                condense_messages.append(value)

        custom_response['data'] = {'message': ' '.join(condense_messages)}

        response.data = custom_response

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def _handle_authentication_error(exc, context, response):
    response.data = {
        'statusCode': response.status_code,
        'status': 'fail',
        'data': {
            'message': 'Please login to continue.',
        },
    }

    return response


def _handle_generic_error(exc, context, response):
    return response

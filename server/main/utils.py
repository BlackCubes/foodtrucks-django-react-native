import random
import string
from django.http import JsonResponse
from django.urls import resolve
from django.utils.text import slugify
from rest_framework import serializers


def get_request_url_name(request_path):
    """
    Gets the URL name from the `urlpatterns`. If there are no URL name, then
    it returns `None`.
    """
    return resolve(request_path).url_name


def get_request_view_name(request_path):
    """
    Gets the name of the view that matches the URL, including the namespace if
    there is one.

    If both `app_name` (or namespace) and the URL name from the `urlpatterns`
    are provided in `urls.py`, then the output would be `app_name:url_name`.

    If only the URL name from the `urlpatterns` is provided in `urls.py`, then
    the output would be `url_name`.

    WEIRD CASES:

    If the `app_name` (or namespace) is provided in `urls.py` with no URL name,
    then the output would be `app_name:app.views.SomeViewSet`.

    If there are no `app_name` (or namespace) and URL name from the `urlpatterns`,
    then the output would be `app.views.SomeViewSet`.
    """
    return resolve(request_path).view_name


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
    Generates a random string.
    """
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    Assumes your instance has a model with a slug field and a name character (char) field.

    Returns: unique slug from the Model's name if the slug query exists in DB, or the newly
    created slug that slugifies the Model's name if the slug query does not exist in DB.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    model = instance.__class__
    queryset_exists = model.objects.filter(slug=slug).exists()

    if queryset_exists:
        unique_slug = '{slug}-{randstr}'.format(
            slug=slug, randstr=random_string_generator(size=4))

        # Run this function again to check if the uniquely random slug is truly unique
        # in the DB. If it is unique, return this unique slug (line 35). Otherwise,
        # generate another unique slug. Rinse and repeat.
        return unique_slug_generator(instance, new_slug=unique_slug)

    return slug


def slug_generator(sender, instance, *args, **kwargs):
    """
    Converts the string into a slug if it is not present.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def error_404(request, exception):
    response = JsonResponse(data={
        'statusCode': 404,
        'status': 'fail',
        'data': {
            'message': 'The requested URL was not found on this server.',
        },
    })

    return response


def error_500(request):
    response = JsonResponse(data={
        'statusCode': 500,
        'status': 'error',
        'data': {
            'message': 'Sorry, a technical error has occured.',
        },
    })

    return response


def final_success_response(response):
    if not response.exception:
        response_data = response.data

        pagination_results = response.data.pop('results', None)
        pagination_meta_data = response.data.pop('meta_data', None)

        if pagination_results is not None and pagination_meta_data is not None:
            response_data = pagination_results

        response.data = {
            'statusCode': response.status_code,
            'status': 'success',
            'data': response_data,
            'meta_data': pagination_meta_data,
        }


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that controls which
    fields should be displayed.

    The `fields` is the wanted fields to be displayed. This should be popped out
    before the superclass, or else the chance of `fields=None` would override `self.fields`.

    The `self.fields` are from the `Meta` class when the serializer is made.

    The `not_wanted_field` is the field that does not occur from the wanted fields, and it
    should not be displayed in the final output.

    Example: If `fields=('uuid', 'name',)` and `self.fields=('uuid', 'name', 'info',)`, then
    `info` would not appear.
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            wanted_fields = set(fields)
            current_fields = set(self.fields.keys())

            for not_wanted_field in current_fields - wanted_fields:
                self.fields.pop(not_wanted_field)

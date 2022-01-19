import random
import string
from django.utils.text import slugify
from django.http import JsonResponse
from rest_framework import serializers


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
        response.data = {
            'statusCode': response.status_code,
            'status': 'success',
            'data': response.data,
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

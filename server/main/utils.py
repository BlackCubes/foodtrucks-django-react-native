import random
import string
from django.utils.text import slugify
from django.http import JsonResponse


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
        'status_code': 404,
        'status': 'fail',
        'data': {
            'message': 'The requested URL was not found on this server.',
        },
    })

    return response


def error_500(request):
    response = JsonResponse(data={
        'status_code': 500,
        'status': 'error',
        'data': {
            'message': 'Sorry, a technical error has occured.',
        },
    })

    return response

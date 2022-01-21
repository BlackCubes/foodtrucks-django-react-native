from rest_framework import serializers

from .models import Review

from main.utils import get_request_view_name

from product.models import Product

from user.models import CustomUser


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer on the Review model.

    Lookup Field: uuid.

    Fields: uuid, review, created_at, updated_at, product, and user.
    """
    product = serializers.SlugRelatedField(
        slug_field='slug', queryset=Product.objects.all(), error_messages={
            'required': 'The product is required.',
            'null': 'The product cannot be empty.',
            'does_not_exist': 'The product does not exist.'})
    review = serializers.CharField(
        max_length=280, error_messages={
            'required': 'The review is required',
            'blank': 'The review cannot be empty.',
            'max_length': 'The review should be no more than 280 characters.'})
    user = serializers.SlugRelatedField(
        slug_field='username', queryset=CustomUser.objects.all(), default=serializers.CurrentUserDefault(), error_messages={
            'does_not_exist': 'User does not exist.'})

    class Meta:
        model = Review
        lookup_field = 'uuid'
        fields = ('uuid', 'review', 'created_at',
                  'updated_at', 'product', 'user',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # This is to check if the it is on the route `/api/v1/reviews/my-reviews/`
        is_auth_user_reviews_route = get_request_view_name(
            self.context['request'].path) == 'reviews:my-reviews'

        if is_auth_user_reviews_route:
            # If it is in the route `/api/v1/reviews/my-reviews/`, then remove
            # the `user` key since this route shows all reviews made by the
            # current authenticated user (removes redundancy).
            representation.pop('user')

        # Checks to see if the `image` field is not empty, or else it won't serialize.
        product_image = None if not instance.product.image else instance.product.image

        representation['product'] = {
            'uuid': str(instance.product.uuid),
            'name': instance.product.name,
            'slug': instance.product.slug,
            'image': product_image,
        }

        return representation

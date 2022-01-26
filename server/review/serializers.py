from rest_framework import serializers

from .models import Review

from main.utils import get_request_view_name

from product.models import Product

from user.models import CustomUser


class ProductRepresentationModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that transforms the `product` field to return an object
    for better description. In the `ReviewSerializer`, the fields (not the `fields`
    in `Meta`) of `product` has a relational serializer field which is the
    `SlugRelatedField`, and this would have an affect on the field to return the
    `slug_field` parameter. This leads to less description. The solution is to
    simply implement `to_representation` method for a better output description on
    this field.
    """

    def get_photo_url(self, image):
        """
        Checks to see if the `image` field is not empty, or else it won't serialize.

        If it isn't empty, then it serializes it.
        """
        request = self.context.get('request', None)

        if request is not None and image and hasattr(image, 'url'):
            image_url = image.url
            return request.build_absolute_uri(image_url)
        else:
            return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        product_image = self.get_photo_url(instance.product.image)

        representation['product'] = {
            'uuid': str(instance.product.uuid),
            'name': instance.product.name,
            'slug': instance.product.slug,
            'image': product_image,
        }

        return representation


class RemoveUserRepresentationSerializer(ProductRepresentationModelSerializer):
    """
    A RepresentationSerializer that removes the `user` field from the outout in
    order to avoid redundancy since we already know what type of authenticated
    user the list of reviews belongs to. This is known if the user is logged in
    and enters the route: `/api/v1/reviews/my-reviews`.

    If one wants to know the detail of this authenticated user, they simply call another
    route: `/api/v1/users/profile`.

    In other words, this route is only concern about getting all reviews from the
    currently logged in authenticated user.

    The route this only targets: `/api/v1/reviews/my-reviews`.
    """

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        is_auth_user_reviews_route = get_request_view_name(
            self.context['request'].path) == 'reviews:my-reviews'

        if is_auth_user_reviews_route:
            representation.pop('user')

        return representation


class RemoveProductRepresentationSerializer(RemoveUserRepresentationSerializer):
    """
    A RepresentationSerializer that removes the `product` field from the output in
    order to avoid redundancy since we already know what type of product the list
    of reviews belongs to. This is known by the product's slug from the nested route:
    `/api/v1/products/<slug>/reviews`.

    If one wants to know the detail of this product, they simply call another route:
    `/api/v1/products/<slug>`.

    In other words, this route is only concern about getting all reviews from the product.

    The route this only targets: `/api/v1/products/<slug>/reviews`.
    """

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        is_reviews_in_product_route = get_request_view_name(
            self.context['request'].path) == 'products:review-list'

        if is_reviews_in_product_route:
            representation.pop('product')

        return representation


class ReviewSerializer(RemoveProductRepresentationSerializer):
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

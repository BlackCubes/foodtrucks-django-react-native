from rest_framework import serializers

from .models import Emoji, Like

from main.utils import get_request_view_name

from product.models import Product


class LikeRepresentationModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that transforms the `emoji` and `product` fields to return
    objects for better description. In the `LikeSerializer`, the fields (not the
    `fields` in `Meta`) of `emoji` and `product` have a relational serializer field
    which is the `SlugRelatedField`, and this would have an affect on both fields
    to return the `slug_field` parameter. This leads to less description. The
    solution is to simply implement the `to_representation` method.
    """

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # This is to check if it is on the route `/api/v1/products/<slug>/socials/`.
        is_socials_in_product_route = get_request_view_name(
            self.context['request'].path) == 'products:social-list'

        representation['emoji'] = {
            'uuid': instance.emoji.uuid,
            'emoji': instance.emoji.emoji,
            'name': instance.emoji.name,
        }

        if is_socials_in_product_route:
            # If it is in the route `/api/v1/products/<slug>/products/`, then remove
            # the `product` key since this route shows all the socials from the
            # product (removes redundancy).
            representation.pop('product')
        else:
            representation['product'] = {
                'uuid': instance.product.uuid,
                'name': instance.product.name,
                'slug': instance.product.slug,
            }

        return representation


class EmojiSerializer(serializers.ModelSerializer):
    """
    Serializer on the Emoji model.

    Lookup Field: uuid.

    Fields: uuid, emoji, and name
    """
    class Meta:
        model = Emoji
        lookup_field = 'uuid'
        fields = ('uuid', 'emoji', 'name',)


class LikeSerializer(LikeRepresentationModelSerializer):
    """
    Serializer on the Like model.

    Fields: uuid, like, emoji, and product.

    On the create method, it checks on two cases: If the object exists, then update
    the like field by incrementing. Otherwise, if the object does not exist, then
    create a new one.
    """
    emoji = serializers.SlugRelatedField(
        slug_field='emoji', queryset=Emoji.objects.all(), error_messages={
            'required': 'The emoji is required.',
            'null': 'The emoji cannot be empty.',
            'does_not_exist': 'The emoji with this icon does not exist.',
            'invalid': 'Invalid value for the emoji.'
        })
    like = serializers.IntegerField(min_value=1, error_messages={
        'required': 'The like is required.',
        'min_value': 'The like should be 1 or greater.',
        'invalid': 'The like needs to be a valid integer.'
    })
    product = serializers.SlugRelatedField(
        slug_field='slug', queryset=Product.objects.all(), error_messages={
            'required': 'The product is required.',
            'null': 'The product cannot be empty.',
            'does_not_exist': 'The product with this slug does not exist.',
            'invalid': 'Invalid value for the product.'
        })

    class Meta:
        model = Like
        fields = ('uuid', 'like', 'emoji', 'product',)

    def create(self, validated_data):
        incoming_uuid = self.initial_data['uuid'] if 'uuid' in self.initial_data else None
        incoming_emoji = self.initial_data['emoji'] if 'emoji' in self.initial_data else None
        incoming_product = self.initial_data['product'] if 'product' in self.initial_data else None

        # If the property exists from the data, proceed.
        if incoming_uuid is not None:
            like_exist = Like.objects.filter(uuid=incoming_uuid).first()

            # If the selected uuid exists in the Like model, proceed.
            if like_exist is not None:
                # If the selected model fields matches both the incoming product and emoji,
                # then increment.
                if like_exist.product.slug == incoming_product and like_exist.emoji.emoji == incoming_emoji:
                    like_exist.like += validated_data['like']
                    like_exist.save()
                    return like_exist

                # Check if the incoming product and emoji still exists since the uuid
                # is incorrect.
                else:
                    likes_available = Like.objects.all()
                    like_exist = {}

                    if len(likes_available):
                        for like_dict in likes_available:
                            if like_dict.product.slug == incoming_product and like_dict.emoji.emoji == incoming_emoji:
                                like_exist = like_dict

                    # If the dictionary is not empty, proceed.
                    if like_exist:
                        like_exist.like += validated_data['like']
                        like_exist.save()
                        return like_exist

        # If the incoming uuid was not provided, check on the incoming emoji and product.
        elif incoming_emoji is not None and incoming_product is not None:
            likes_available = Like.objects.all()
            like_exist = {}

            if len(likes_available):
                for like_dict in likes_available:
                    if like_dict.product.slug == incoming_product and like_dict.emoji.emoji == incoming_emoji:
                        like_exist = like_dict

            # If the dictionary is not empty, proceed.
            if like_exist:
                like_exist.like += validated_data['like']
                like_exist.save()
                return like_exist

        # In all failed cases, this is most likely a new creation.
        new_like = Like.objects.create(**validated_data)
        return new_like

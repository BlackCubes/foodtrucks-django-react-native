from rest_framework import serializers

from .models import Emoji, Like
from foodtruck.models import Product


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer on the Like model.

    Fields: uuid, like, emoji, and product.

    On the create method, it checks on two cases: If the object exists, then update
    the like field by incrementing. Otherwise, if the object does not exist, then
    create a new one.
    """
    emoji = serializers.SlugRelatedField(
        slug_field='emoji', queryset=Emoji.objects.all())
    product = serializers.SlugRelatedField(
        slug_field='slug', queryset=Product.objects.all())

    class Meta:
        model = Like
        fields = ('uuid', 'like', 'emoji', 'product',)

    def create(self, validated_data):
        like_uuid = self.initial_data['uuid'] if 'uuid' in self.initial_data else None

        # If the property exists from the data, proceed.
        if like_uuid is not None:
            like_exist = Like.objects.filter(uuid=like_uuid).first()

            # If the selected uuid exists in the Like model, then increment.
            # Otherwise, it does not exist, then create a new one.
            if like_exist is not None:
                like_exist.like += validated_data['like']
                like_exist.save()
                return like_exist

        new_like = Like.objects.create(**validated_data)
        return new_like


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

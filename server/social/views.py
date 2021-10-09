from rest_framework import generics

from .models import Emoji, Like
from .serializers import EmojiSerializer, LikeSerializer


# Emoji views:
class EmojiListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the Emoji model.

    Request Type: GET.
    """
    queryset = Emoji.objects.all()
    serializer_class = EmojiSerializer


class EmojiDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Emoji model based on its uuid.

    Lookup Field: uuid.

    Request Type: GET.
    """
    queryset = Emoji.objects.all()
    lookup_field = 'uuid'
    serializer_class = EmojiSerializer


# Like views:
class LikeListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to either retrieve a list or create (or update from the custom method)
    from the Like model.

    Request Type: GET and POST.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve or update from the Like model based on its uuid.

    Lookup Field: uuid.

    Request Type: GET, PUT, and PATCH.
    """
    queryset = Like.objects.all()
    lookup_field = 'uuid'
    serializer_class = LikeSerializer

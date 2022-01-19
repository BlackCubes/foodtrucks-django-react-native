from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Emoji, Like
from .serializers import EmojiSerializer, LikeSerializer

from main.utils import final_success_response


# Emoji views:
class EmojiListAPIView(generics.ListAPIView):
    """
    API view to retrieve a list from the Emoji model.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = EmojiSerializer
    queryset = Emoji.objects.all()

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)


class EmojiDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve one from the Emoji model based on its uuid.

    Lookup Field: uuid.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = EmojiSerializer
    queryset = Emoji.objects.all()
    lookup_field = 'uuid'

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)


# Like views:
class LikeListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to either retrieve a list or create (or update from the custom method)
    from the Like model.

    Request Type: GET and POST.
    """
    permission_classes = (AllowAny,)
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)


class LikeDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve the Like model based on its uuid.

    Lookup Field: uuid.

    Request Type: GET.
    """
    permission_classes = (AllowAny,)
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    lookup_field = 'uuid'

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(response)

        return super().finalize_response(request, response, *args, **kwargs)

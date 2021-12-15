from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .renderers import UserJSONRenderer
from .serializers import LoginSerializer, RegisterSerializer


class LoginAPIView(APIView):
    """
    API view to login the user if it exists in the User model.

    Permissions: Allow any.

    Renderers: UserJSONRenderer.

    Serializer: LoginSerializer.

    Request Type: POST.
    """
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serialzer_class = LoginSerializer

    def post(self, request):
        serializer = self.serialzer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = {
            'status': 'success',
            'data': serializer.data,
        }

        return Response(data=data, status=status.HTTP_200_OK)


class RegisterAPIView(APIView):
    """
    API view to create a new user to the User model.

    Permissions: Allow any.

    Renderers: UserJSONRenderer.

    Serializer: RegisterSerializer.

    Request Type: POST.
    """
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'status': 'success',
            'data': serializer.data,
        }

        return Response(data=data, status=status.HTTP_201_CREATED)

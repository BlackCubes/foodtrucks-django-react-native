from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .renderers import UserJSONRenderer
from .serializers import ChangePasswordSerializer, LoginSerializer, RegisterSerializer, UserProfileSerializer


class ChangePasswordUpdateAPIView(UpdateAPIView):
    """
    API view to update a user's password to the User model.

    Permissions: IsAuthenticated.

    Renderers: UserJSONRenderer.

    Serializer: ChangePasswordSerializer.

    Request Type: PUT and PATCH.
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'statusCode': status.HTTP_200_OK,
            'status': 'success',
            'data': serializer.data,
        }

        return Response(data=data, status=status.HTTP_200_OK)


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
            'statusCode': status.HTTP_200_OK,
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
            'statusCode': status.HTTP_201_CREATED,
            'status': 'success',
            'data': serializer.data,
        }

        return Response(data=data, status=status.HTTP_201_CREATED)


class UserProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    API view to either retrieve or update a user to the User model.

    Permissions: IsAuthenticated.

    Renderers: UserJSONRenderer.

    Serializer: UserProfileSerializer.

    Request Type: GET, PUT, and PATCH.
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            'statusCode': status.HTTP_200_OK,
            'status': 'success',
            'data': serializer.data,
        }

        return Response(data=data, status=status.HTTP_200_OK)

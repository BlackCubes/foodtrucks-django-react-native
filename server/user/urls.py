from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('profile/', views.UserProfileRetrieveUpdateAPIView.as_view()),
]

from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('profile/', views.UserProfileRetrieveUpdateAPIView.as_view(), name='profile'),
    path('change-password/', views.ChangePasswordUpdateAPIView.as_view(),
         name='change-password'),
]

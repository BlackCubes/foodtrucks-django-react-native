from django.urls import path

from . import views


urlpatterns = [
    path('', views.ReviewListCreateAPIView.as_view()),
    path('<uuid:uuid>', views.ReviewDetailUpdateDeleteAPIView.as_view()),
    path('my-reviews', views.ReviewListAPIView.as_view(), name='my-reviews'),
]

from django.urls import path

from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewListCreateAPIView.as_view(), name='list-create'),
    path('<uuid:uuid>', views.ReviewDetailUpdateDeleteAPIView.as_view(),
         name='detail-update-delete'),
    path('my-reviews', views.ReviewListAPIView.as_view(), name='my-reviews'),
]

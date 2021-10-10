from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
    path('<slug:slug>', views.ProductDetailAPIView.as_view()),
]

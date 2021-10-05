from django.urls import path

from . import views

urlpatterns = [
    path('', views.TruckListAPIView.as_view()),
    path('<slug:slug>', views.TruckDetailAPIView.as_view()),
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<slug:slug>', views.ProductDetailAPIView.as_view()),
]

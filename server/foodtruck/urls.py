from django.urls import path

from . import views

urlpatterns = [
    path('', views.TruckListAPIView.as_view()),
    path('<slug:slug>', views.TruckDetailAPIView.as_view()),
]

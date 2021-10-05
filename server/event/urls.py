from django.urls import path

from . import views


urlpatterns = [
    path('', views.EventListAPIView.as_view()),
    path('<uuid:uuid>', views.EventDetailAPIView.as_view()),
]

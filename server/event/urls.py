from django.urls import path

from . import views


app_name = 'events'

urlpatterns = [
    path('', views.EventListAPIView.as_view(), name='list'),
    path('<uuid:uuid>', views.EventDetailAPIView.as_view(), name='detail'),
]

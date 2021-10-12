from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.TruckListAPIView.as_view()),
    path('<slug:slug>', views.TruckDetailAPIView.as_view()),
    re_path(r'^(?P<truck_slug>[\w-]+)/products/?$',
            views.TruckProductsModelViewSet.as_view({'get': 'list'})),
    re_path(r'^(?P<truck_slug>[\w-]+)/reviews/?$',
            views.TruckReviewsModelViewSet.as_view({'get': 'list'})),
    re_path(r'^(?P<truck_slug>[\w-]+)/socials/?$',
            views.TruckLikesModelViewSet.as_view({'get': 'list'})),
]

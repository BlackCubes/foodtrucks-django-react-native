from django.urls import path, re_path

from . import views


app_name = 'foodtrucks'

urlpatterns = [
    path('', views.TruckListAPIView.as_view(), name='list'),
    path('<slug:slug>', views.TruckDetailAPIView.as_view(), name='detail'),
    re_path(r'^(?P<truck_slug>[\w-]+)/events/?$',
            views.TruckEventsModelViewSet.as_view({'get': 'list'}), name='event-list'),
    re_path(r'^(?P<truck_slug>[\w-]+)/products/?$',
            views.TruckProductsModelViewSet.as_view({'get': 'list'}), name='product-list'),
    re_path(r'^(?P<truck_slug>[\w-]+)/reviews/?$',
            views.TruckReviewsModelViewSet.as_view({'get': 'list'}), name='review-list'),
    re_path(r'^(?P<truck_slug>[\w-]+)/socials/?$',
            views.TruckLikesModelViewSet.as_view({'get': 'list'}), name='social-list'),
]

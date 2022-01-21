from django.urls import path, re_path

from . import views


app_name = 'products'

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='list'),
    path('<slug:slug>', views.ProductDetailAPIView.as_view(), name='detail'),
    re_path(r'^(?P<product_slug>[\w-]+)/reviews/?$',
            views.ProductReviewsModelViewSet.as_view({'get': 'list'}), name='review-list'),
    re_path(r'^(?P<product_slug>[\w-]+)/socials/?$',
            views.ProductLikesModelViewSet.as_view({'get': 'list'}), name='social-list'),
]

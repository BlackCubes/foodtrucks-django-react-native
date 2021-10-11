from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
    path('<slug:slug>', views.ProductDetailAPIView.as_view()),
    re_path(r'^(?P<product_slug>[\w-]+)/socials/?$',
            views.ProductLikesModelViewSet.as_view({'get': 'list'})),
]

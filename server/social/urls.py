from django.urls import path

from . import views


app_name = 'socials'

urlpatterns = [
    path('', views.LikeListCreateAPIView.as_view(), name='list-create'),
    path('<uuid:uuid>', views.LikeDetailAPIView.as_view(), name='detail'),
    path('emojis/', views.EmojiListAPIView.as_view(), name='emoji-list'),
    path('emojis/<uuid:uuid>', views.EmojiDetailAPIView.as_view(), name='emoji-detail'),
]

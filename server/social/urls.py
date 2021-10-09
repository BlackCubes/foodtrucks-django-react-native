from django.urls import path

from . import views


urlpatterns = [
    path('', views.LikeListCreateAPIView.as_view()),
    path('<uuid:uuid>', views.LikeDetailUpdateAPIView.as_view()),
    path('emojis/', views.EmojiListAPIView.as_view()),
    path('emojis/<uuid:uuid>', views.EmojiDetailAPIView.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'), # Посилання для нового поста
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'), # Посилання для коментаря
]
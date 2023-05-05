from django.urls import path
from blog.views import *

urlpatterns = [
    # Для главной странице обращаемся к классу Home из views.py
    path('', Home.as_view(), name='home'),
    # Django ожидает либо pk, либо slug
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
]

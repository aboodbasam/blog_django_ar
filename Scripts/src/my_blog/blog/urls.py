from django.urls import path
from src.my_blog.blog import views

urlpatterns = [
    path('', views.home, name='home')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
    path('from', views.form, name='form'),
    path('post_list', views.post_list, name='post_list'),
]


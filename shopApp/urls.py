from django.contrib import admin
from django.urls import path
from shopApp.views import index, about

urlpatterns = [
    path('',index, name='index'),
    path('about/', about, name='about'),
]
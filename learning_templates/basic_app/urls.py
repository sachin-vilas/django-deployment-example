from django.urls import path,include
from django.contrib import admin
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('relative', views.relative, name='relative'),
    path('other', views.other, name='other'),
]

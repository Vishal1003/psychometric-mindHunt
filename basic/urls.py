from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='basic-home'),
    path('form/', views.test, name='basic-form'),
]

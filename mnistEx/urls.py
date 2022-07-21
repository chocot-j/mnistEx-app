from django.urls import path

from . import views


app_name = 'mnistEx'

urlpatterns = [
    path('', views.index, name='index'),
    path('guess/', views.guess, name='guess'),
]
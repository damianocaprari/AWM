
from django.urls import path
from . import views


app_name = 'conditions'

urlpatterns = [
    path('', views.index, name='index'),
]


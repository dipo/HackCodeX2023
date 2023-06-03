from django.urls import path

from . import views

app_name = 'able'

urlpatterns = [
    # ex: /able/
    path('', views.index, name='index'),
]
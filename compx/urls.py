
from django.urls import path
from . import views

urlpatterns = [
    path('', views.compHome, name='compHome'),
    path('compxdet/', views.compxdet, name='compxdet'),

]


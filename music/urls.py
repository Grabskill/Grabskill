from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #/music/id/
    path('<str:album_id>/', views.detail, name='detail'),
]
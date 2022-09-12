from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'pracice'

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    #path('', views.add_book(), name='homepage'),
    #/book/id/
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    path('add_book/', views.add_book, name="add_book"),
]
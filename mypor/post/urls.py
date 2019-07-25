from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
     path('', views.IndexView.as_view(), name='main'),
     #path('', views.main, name='main'),
     path('new', views.post_new, name='post_new'),
     
]
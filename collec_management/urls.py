from django.urls import path
from . import views


urlpatterns = [
    path('', views.collection_list, name='home'), 
    path('about/', views.about, name='about'),
    path('all/', views.collection_list, name='collection_list'),
]

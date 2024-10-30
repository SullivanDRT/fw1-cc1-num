from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('new/', views.ajouter_collec, name="ajouter_collec")
]

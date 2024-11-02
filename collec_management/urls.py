from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('collection/<int:id_collec>/', views.collec_details, name = 'collec_dtails'),
]

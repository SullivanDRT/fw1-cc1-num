from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about, name="about"),
    path("new/", views.ajouter_collec, name="ajouter_collec"),
    path("delete/<int:collec_id>", views.supprimmer_collec, name="supprimmer_collec"),
    path(
        "delete_comfirm/<int:collec_id>",
        views.comfirmation_suppression_collec,
        name="comfirmation_suppression_collec",
    ),
    path("change/<int:collec_id>", views.modifier_collec, name="modifier_collec"),
    path('', views.collection_list, name='home'),
    path('all/', views.collection_list, name='collection_list'),
    path('collection/<int:id_collec>/', views.collec_details, name = 'collec_details'),
]

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
]

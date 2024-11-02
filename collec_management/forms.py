from .models import Collec
from django.forms import ModelForm

class CollecForm(ModelForm):
    class Meta:
        model = Collec
        fields = ["title", "description"]
        labels = {
            "title": "Titre"
        }
        
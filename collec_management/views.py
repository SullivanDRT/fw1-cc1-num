from django.shortcuts import render

# Create your views here.
from .models import Collec

def collection_list(request):
    collections = Collec.objects.all()  
    return render(request, 'collec_management/collection_list.html', {'collections': collections})


def about(request):
    return render(request, 'collec_management/about.html')


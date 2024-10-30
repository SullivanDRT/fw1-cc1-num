from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Collec

# Create your views here.


def about(request):
    return render(request, 'collec_management/about.html')

def collec_details(request, id_collec):
    collection = get_object_or_404(Collec ,id=id_collec)
    context = {'collection' : collection}
    return render(request, 'collec_management/collec_details.html', context)


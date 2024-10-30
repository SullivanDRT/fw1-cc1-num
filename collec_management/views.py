from django.shortcuts import render, redirect
from .forms import CollecForm
from django.utils import timezone
from django.http import HttpResponse


# Create your views here.


def about(request):
    return render(request, 'collec_management/about.html')


def ajouter_collec(request):
    if request.method == "POST":
        form = CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit= False)
            collection.date = timezone.now()
            collection.save()
            return HttpResponse("La collection s'est bien ajoutée à la bd, redirection faire la fiche détails à faire")
    else:
        form = CollecForm()
    context = {'form': form}
    return render(request, 'collec_management/ajouter_collec.html', context)
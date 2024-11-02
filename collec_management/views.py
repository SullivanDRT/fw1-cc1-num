from django.shortcuts import render, redirect, get_object_or_404
from .models import Collec
from .forms import CollecForm
from django.utils import timezone
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from .models import Collec

def collection_list(request):
    collections = Collec.objects.all()  
    return render(request, 'collec_management/collection_list.html', {'collections': collections})


def about(request):
    return render(request, "collec_management/about.html")


def ajouter_collec(request):
    if request.method == "POST":
        form = CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.date = timezone.now()
            collection.save()
            return HttpResponse(
                "La collection s'est bien ajoutée à la bd, redirection faire la fiche détails à faire"
            )
    else:
        form = CollecForm()
    context = {"form": form}
    return render(request, "collec_management/ajouter_collec.html", context)


def supprimmer_collec(request, collec_id):
    if request.method == "POST":
        try:
            collec = Collec.objects.get(pk=collec_id)
        except Collec.DoesNotExist:
            raise Http404("la collection n'existe pas")
        collec.delete()
        return HttpResponseRedirect("/all")
    else:
        return HttpResponseRedirect(f"/delete_comfirm/{collec_id}")


def comfirmation_suppression_collec(request, collec_id):
    try:
        collec = Collec.objects.get(pk=collec_id)
    except Collec.DoesNotExist:
        raise Http404("la collection n'existe pas")
    if request.method == "POST":
        collec.delete()
        return HttpResponseRedirect("/all")
    else:
        return render(
            request,
            "collec_management/comfirmation_suppression_collec.html",
            {"collec": collec},
        )



def modifier_collec(request, collec_id):
    try:
        collec = Collec.objects.get(pk=collec_id)
    except Collec.DoesNotExist:
        raise Http404("la collection n'existe pas")
    if request.method == "POST":
        updated_collec = CollecForm(request.POST, instance=collec)
        updated_collec.save()
        return HttpResponseRedirect("/all")
    else:
        form = CollecForm(instance=collec)
        return render(
            request,
            "collec_management/modifier_collec.html",
            {"form": form, "collec": collec},
        )

def collec_details(request, id_collec):
    collection = get_object_or_404(Collec ,id=id_collec)
    context = {'collection' : collection}
    return render(request, 'collec_management/collec_details.html', context)


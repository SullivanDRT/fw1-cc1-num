from django.shortcuts import render, redirect
from .models import Collec
from .forms import CollecForm
from django.utils import timezone
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your views here.


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
        return HttpResponseRedirect("/about")
    else:
        return HttpResponseRedirect(f"/delete_comfirm/{collec_id}")


def comfirmation_suppression_collec(request, collec_id):
    try:
        collec = Collec.objects.get(pk=collec_id)
    except Collec.DoesNotExist:
        raise Http404("la collection n'existe pas")
    if request.method == "POST":
        collec.delete()
        return HttpResponseRedirect("/about")
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
        return HttpResponseRedirect("/about")
    else:
        form = CollecForm(instance=collec)
        return render(
            request,
            "collec_management/modifier_collec.html",
            {"form": form, "collec": collec},
        )

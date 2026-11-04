from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegisterParcelForm
from .models import Parcel


#liste colis
colis_data=["colis1", "colis2", "colis3"]

def tracking_page(request):
    parcel = None
    error = None
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        try:
            parcel = Parcel.objects.get(tracking_number=tracking_number)
        except Parcel.DoesNotExist:
            error = "Colis non trouvé"
    return render(request, "tracking.html", {"parcel": parcel, "error": error})



# Create your views here.
def homepage(request):
    nom_entrepot = "Entrepôt Central"  # Exemple de nom d'entrepôt
    nb_colis = len(Parcel.objects.all())  # Exemple de nombre de colis
    return render(request, "index.html",context={'nb_colis': nb_colis,'nom_entrepot' : nom_entrepot})


def parcels_page (request):
    return render(request, "parcels.html", context={"colis_data": Parcel.objects.all()})

def add_parcel_page(request):
    form = RegisterParcelForm()
    if request.method == 'POST':
        form = RegisterParcelForm(request.POST)
        if form.is_valid():
            form.save() #insertion dans la base de données
            return HttpResponse("Colis ajouté avec succès !")
    else:
        form=RegisterParcelForm()
        return render(request, "add_parcel.html", context={'form': form})
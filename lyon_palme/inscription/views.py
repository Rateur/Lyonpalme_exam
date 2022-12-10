from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

from .regex import Regex
from .forms import Formulaire_inscription
from .models import Inscription

def inscription_form(request):
    if request.method == 'POST':
        form = Formulaire_inscription(request.POST)
        if form.is_valid() and Regex.verif_mail(form.cleaned_data['mail']) and Regex.verif_tel(form.cleaned_data['telephone']) and Regex.verif_cp(form.cleaned_data['code_postal']):
            reussi = "réussi"
            adherent = Inscription()
            adherent.nom = request.POST['nom']
            adherent.prenom = request.POST['prenom']
            adherent.date_naissance = request.POST['date_naissance']
            adherent.mail = request.POST['mail']
            adherent.telephone = request.POST['telephone']
            adherent.adresse = request.POST['adresse']
            adherent.date_inscription = timezone.now()
            adherent.date_certificat = request.POST['date_certificat']
            adherent.save()
            return render(request, 'inscription/inscription_form.html', {'form' : form, 'reussi' : reussi})
        else:
            erreur_mail = ""
            erreur_tel = ""
            erreur_cp = ""

            if not Regex.verif_mail(form.cleaned_data['mail'])
                erreur_mail = "Mauvais format d'adresse mail"
            if not Regex.verif_tel(form.cleaned_data['telephone']):
                erreur_tel = "Mauvais format de numéro de téléphone : les chiffres doivent être séparés par des points, des tirets ou des espaces"
            if not Regex.verif_cp(form.cleaned_data['code_postal']):
                erreur_cp = "Mauvais format de code postal"
            context = {
                'form' : form,
                'erreur_mail' : erreur_mail,
                'erreur_tel' : erreur_tel,
                'erreur_cp' : erreur_cp
            }
            return render(request, 'inscription/inscription_form.html', context)
    else:
        form = Formulaire_inscription()
    
    return render(request, 'inscription/inscription_form.html', {'form' : form})

def politique_confidentialite(request):
    return render(request, 'inscription/politique_confidentialite.html')
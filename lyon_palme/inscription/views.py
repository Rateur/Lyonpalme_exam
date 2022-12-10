from django.shortcuts import render
from django.http import HttpResponseRedirect

from .regex import Regex
from .forms import Formulaire_inscription

def inscription_form(request):
    if request.method == 'POST':
        form = Formulaire_inscription(request.POST)
        if form.is_valid() and Regex.verif_mail(form.cleaned_data['mail']) and Regex.verif_tel(form.cleaned_data['tel']) and Regex.verif_cp(form.cleaned_data['cp']):#REMPLACER LES NOMS ENTRE GUILLEMETS PAR LES NOMS DES CASES DU FORMULAIRE 
            return render(request, 'inscription/inscription_form.html', {'form' : form})
        else:
            erreur_mail = ""
            erreur_tel = ""
            erreur_cp = ""

            if not Regex.verif_mail(form.cleaned_data['mail']):#REMPLACER LES NOMS ENTRE GUILLEMETS PAR LES NOMS DES CASES DU FORMULAIRE 
                erreur_mail = "Mauvais format d'adresse mail"
            if not Regex.verif_tel(form.cleaned_data['tel']):
                erreur_mail = "Mauvais format de numéro de téléphone : les chiffres doivent être séparés par des points, des tirets ou des espaces"
            if not Regex.verif_cp(form.cleaned_data['cp']):
                erreur_mail = "Mauvais format de code postal"
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
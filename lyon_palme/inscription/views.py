from django.shortcuts import render
from django.http import HttpResponseRedirect

from .regex import Regex

def inscription_form(request):
    if request.method == 'POST':
        form = Formulaire_inscription(request.POST)
        if form.is_valid() and Regex.verif_mail(form.cleaned_data['nom']):
            return render(request, 'inscription/inscription_form.html', {'form' : form})
        else:
            erreur_mail = ""
            if not Regex.verif_mail(form.cleaned_data['nom']):
                erreur_mail = "Mauvais format d'adresse mail"
            return render(request, 'inscription/inscription_form.html', {'form' : form, 'erreur_mail' : erreur_mail})
    else:
        form = Formulaire_inscription()
    
    return render(request, 'inscription/inscription_form.html', {'form' : form})
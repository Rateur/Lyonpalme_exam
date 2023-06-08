from django.urls import path
from . import views
app_name='inscription'

urlpatterns = [
    path('inscription_form', views.inscription_form, name='inscription_form'),
    path('politique_confidentialite', views.politique_confidentialite, name='politique_confidentialite'),
    path('login_nageur', views.login_nageur, name='login_nageur'),
    path('login_secretaire', views.login_secretaire, name='login_secretaire'),
    path('change_password', views.change_password, name='change_password'),
    path('accueil_secretaire', views.accueil_secretaire, name='accueil_secretaire'),
    path('accueil_secretaire/<int:adherent_id>/', views.nageur, name="nageur"),
    path('accueil_secretaire/<int:adherent_id>/modification_nageur',views.modification_nageur, name="modification_nageur"),
    path('accueil_secretaire/<int:adherent_id>/archiver_nageur', views.archiver_nageur, name="archiver_nageur"),
    path('accueil_nageur', views.accueil_nageur, name='accueil_nageur'),
    path('accueil_nageur/trombinoscope/', views.trombinoscope, name='trombinoscope'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('', views.Accueil, name="Accueil")
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
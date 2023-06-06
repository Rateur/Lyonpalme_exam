from django.urls import path
from . import views
app_name='inscription'

urlpatterns = [
    path('inscription_form', views.inscription_form, name='inscription_form'),
    path('politique_confidentialite', views.politique_confidentialite, name='politique_confidentialite'),
    path('login', views.login_view, name='login'),
    path('change_password', views.change_password, name='change_password'),
    path('AccueilSecretaire', views.AccueilSecretaire, name='AccueilSecretaire'),
    path('AccueilSecretaire/<int:adherent_id>/', views.nageur, name="nageur"),
    path('AccueilSecretaire/<int:adherent_id>/modification_nageur',views.modification_nageur, name="modification_nageur")
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
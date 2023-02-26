from django.urls import path
from . import views
app_name='inscription'

urlpatterns = [
    path('inscription_form', views.inscription_form, name='inscription_form'),
    path('politique_confidentialite', views.politique_confidentialite, name='politique_confidentialite'),
    path('login', views.login, name='login')
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from .views import MiPerfilUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('editar_perfil', MiPerfilUpdateView.as_view(), name='editar_perfil'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

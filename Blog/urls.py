from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('articulos/', views.lista_articulos, name='lista_articulos'),
    path('articulos/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('editar_articulo/<int:pk>/', views.editar_articulo, name='editar_articulo'),
    path('eliminar_articulo/<int:pk>/', views.eliminar_articulo, name='eliminar_articulo'),
]

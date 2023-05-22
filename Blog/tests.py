from django.test import TestCase
from django.contrib.auth.models import User
from .models import Perfil, Articulo

class ArticuloModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='usuario_prueba', password='contraseña_prueba')
        perfil = Perfil.objects.create(user=user, nombre='Autor de prueba')

        Articulo.objects.create(
            id=1,
            titulo="Título de prueba",
            subtitulo="Subtítulo de prueba",
            cuerpo="Cuerpo del artículo de prueba",
            autor=perfil,
            imagen="ruta/de/imagen.jpg"
        )
        
    def test_creacion_articulo(self):
        articulo = Articulo.objects.get(id=1)
        self.assertEqual(Articulo.objects.count(), 1)
        self.assertEqual(articulo.titulo, "Título de prueba")
        self.assertEqual(articulo.subtitulo, "Subtítulo de prueba")
        self.assertEqual(articulo.cuerpo, "Cuerpo del artículo de prueba")
        self.assertEqual(articulo.autor.nombre, "Autor de prueba")
        self.assertEqual(articulo.imagen, "ruta/de/imagen.jpg")

    def test_articulo_str(self):
        articulo = Articulo.objects.get(id=1)
        expected_str = "Título de prueba"
        self.assertEqual(articulo.__str__(), expected_str)


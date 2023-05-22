from django.test import TestCase
from django.contrib.auth.models import User
from .models import Perfil

class PerfilModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='usuario_prueba', password='contraseña_prueba')
        Perfil.objects.create(user=user, nombre='Nombre de prueba', descripcion='Descripción de prueba')

    def test_relacion_usuario(self):
        perfil = Perfil.objects.get(id=1)
        self.assertEqual(perfil.user.username, 'usuario_prueba')

    def test_campos_adicionales(self):
        perfil = Perfil.objects.get(id=1)
        self.assertEqual(perfil.nombre, 'Nombre de prueba')
        self.assertEqual(perfil.descripcion, 'Descripción de prueba')

    def test_metodo_str(self):
        perfil = Perfil.objects.get(id=1)
        self.assertEqual(perfil.__str__(), 'usuario_prueba')

    def test_campos_opcionales(self):
        perfil = Perfil.objects.create(user=User.objects.create_user(username='usuario_prueba2', password='contraseña_prueba2'), nombre='Nombre de prueba 2')
        self.assertTrue(not perfil.avatar)
        self.assertEqual(perfil.descripcion, '')


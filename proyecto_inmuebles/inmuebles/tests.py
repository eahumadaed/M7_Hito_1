from django.test import TestCase
from .models import Usuario, TipoUsuario, Region, Comuna

class UsuarioModelTest(TestCase):
    def setUp(self):
        region = Region.objects.create(nombre='Metropolitana')
        comuna = Comuna.objects.create(nombre='Santiago', region=region)
        tipo_usuario = TipoUsuario.objects.create(descripcion='Arrendatario')
        Usuario.objects.create(
            nombres='Juan',
            apellidos='Perez',
            rut='12345678-9',
            direccion='Calle Falsa 123',
            telefono='987654321',
            email='juan.perez@example.com',
            tipo_usuario=tipo_usuario,
            comuna=comuna,
            region=region
        )

    def test_usuario_creation(self):
        usuario = Usuario.objects.get(email='juan.perez@example.com')
        self.assertEqual(usuario.nombres, 'Juan')
        self.assertEqual(usuario.apellidos, 'Perez')

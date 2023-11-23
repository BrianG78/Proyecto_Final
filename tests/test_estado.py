from django.test import TestCase
from api.models import Estado

class test_estado(TestCase):
    def setUp(self):
        Estado.objects.create(idEstado = 1, estado="Hidalgo")

    def test_municipio(self):
        objeto = Estado.objects.get(idEstado = 1)
        
        self.assertEqual(objeto.estado, "Hidalgo")
        
    def TearDown(self):
        Estado.objects.all().delete()
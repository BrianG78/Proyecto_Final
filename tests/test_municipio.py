from django.test import TestCase
from api.models import Estado, Municipio

class test_municipio(TestCase):
    def setUp(self):
        estado = Estado.objects.create(idEstado = 1, estado="Hidalgo")
        Municipio.objects.create(idMunicipio = 1, municipio = "muni", fk_estado=estado)
        
    def test_municipio(self):
        objeto = Municipio.objects.get(idMunicipio = 1)
        
        self.assertEqual(objeto.municipio, "muni")
        
    def TearDown(self):
        Estado.objects.all().delete()
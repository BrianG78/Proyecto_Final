from django.test import TestCase
from api.models import Salon, Municipio, TipoSalon, Estado

class test_municipio(TestCase):
    def setUp(self):
        estado = Estado.objects.create(idEstado = 1, estado="Hidalgo")
        municipio = Municipio.objects.create(idMunicipio = 1, municipio = "muni", fk_estado=estado)
        tiposalon = TipoSalon.objects.create(idTipoSalon = 1, descripcion="Fiestas", status = 1)
        Salon.objects.create(idSalon = 1, fk_TipoSalon = tiposalon, fk_Municipio = municipio, descripcion = "algo", tamano = "10x10")
        
    def test_municipio(self):
        objeto = Salon.objects.get(idSalon = 1)
        
        self.assertEqual(objeto.descripcion, "algo")
        
    def TearDown(self):
        Salon.objects.all().delete()
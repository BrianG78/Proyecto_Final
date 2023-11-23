from django.test import TestCase
from api.models import TipoSalon

class test_estado(TestCase):
    def setUp(self):
        TipoSalon.objects.create(idTipoSalon = 1, descripcion="Fiestas", status = 1)

    def test_municipio(self):
        objeto = TipoSalon.objects.get(idTipoSalon = 1)
        
        self.assertEqual(objeto.descripcion, "Fiestas")
        
    def TearDown(self):
        TipoSalon.objects.all().delete()
from django.db import models

# Create your models here.

class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True, db_column='idEstado')
    estado = models.CharField(max_length=25, db_column='estado')
    class Meta:
        db_table = 'Estado'
        
class Municipio(models.Model):
    idMunicipio = models.AutoField(primary_key=True, db_column='idMunicipio')
    municipio = models.CharField(max_length=25, db_column='municipio')
    fk_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1, db_column='fk_estado')
    class Meta:
        db_table = 'Municipio'
        
class TipoSalon(models.Model):
    idTipoSalon = models.AutoField(primary_key=True, db_column='idTipoSalon')
    descripcion = models.CharField(max_length=25, db_column='descripcion')
    status = models.IntegerField(blank=False, db_column='status')
    class Meta:
        db_table = 'TipoSalon' 

class Salon(models.Model):
    idSalon = models.AutoField(primary_key=True, db_column='idSalon')
    fk_TipoSalon = models.ForeignKey(TipoSalon, on_delete=models.CASCADE, default=1, db_column='fk_TipoSalon')
    fk_Municipio =models.ForeignKey(Municipio, on_delete=models.CASCADE, default=1, db_column='fk_Municipio')
    descripcion = models.TextField(db_column='descripcion')
    tamano = models.TextField(db_column='tamano')
    class Meta:
        db_table = 'Salon'
    
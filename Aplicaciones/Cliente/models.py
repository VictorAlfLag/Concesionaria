from django.db import models
# Create your models here.

class Ciudad(models.Model):
    id_ciu = models.AutoField(primary_key=True)
    nombre_ciu = models.CharField(max_length=50)

    class Meta:
        managed = False  # Indica que Django no gestione esta tabla
        db_table = 'ciudad'  # Nombre exacto de la tabla en la base de datos

class Propietario(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nombre_pro = models.CharField(max_length=50)
    apellido_pro = models.CharField(max_length=50)
    email_pro = models.CharField(max_length=100)
    telefono_pro = models.CharField(max_length=15)
    fkid_ciu = models.ForeignKey(Ciudad, on_delete=models.CASCADE, db_column='fkid_ciu')
    
    class Meta:
        managed = False  # Indica que Django no gestione esta tabla
        db_table = 'propietario'  # Nombre exacto de la tabla en la base de datos
   
class Modelo(models.Model):
    id_mod = models.AutoField(primary_key=True)
    nombre_mod = models.CharField(max_length=50)

    class Meta:
        managed = False  # Indica que Django no gestione esta tabla
        db_table = 'modelo'  # Nombre exacto de la tabla en la base de datos
     
class Color(models.Model):
    id_col = models.AutoField(primary_key=True)
    nombre_col = models.CharField(max_length=50)

    class Meta:
        managed = False  # Indica que Django no gestione esta tabla
        db_table = 'color'  # Nombre exacto de la tabla en la base de datos
        
class Vehiculo(models.Model):
    id_veh = models.AutoField(primary_key=True)
    anio_veh = models.IntegerField()
    placa_veh = models.CharField(max_length=25)
    fkid_mod = models.ForeignKey(Modelo, on_delete=models.CASCADE, db_column='fkid_mod')
    fkid_col = models.ForeignKey(Color, on_delete=models.CASCADE, db_column='fkid_col')
    
    class Meta:
        managed = False  # Indica que Django no gestione esta tabla
        db_table = 'vehiculo'  # Nombre exacto de la tabla en la base de datos
        
class Factura(models.Model):
    id_fac = models.AutoField(primary_key=True)
    precio_fac = models.DecimalField(max_digits=10, decimal_places=2)
    fkid_pro = models.ForeignKey(Propietario, on_delete=models.CASCADE, db_column='fkid_pro')
    fkid_veh = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, db_column='fkid_veh')
    
    class Meta:
        managed = False  # Indica que Django no gestione esta tabla
        db_table = 'factura'  # Nombre exacto de la tabla en la base de datos

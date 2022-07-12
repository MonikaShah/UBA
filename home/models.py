# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class uba(models.Model):
   # id = models.CharField(primary_key=True, max_length=20)
    id = models.BigIntegerField(primary_key=True, max_length=20)
    #geom = models.GeometryField(blank=True, null=True)
    Ward_No= models.BigIntegerField(blank=True, null=True)
    schedule_filled_by_name = models.CharField(max_length=254, blank=True, null=True)
    Block = models.CharField(max_length=254, blank=True, null=True)
    habitations = models.CharField(max_length=254, blank=True, null=True)
    gram_panchayat= models.CharField(max_length=254, blank=True, null=True)
    District = models.CharField(max_length=254, blank=True, null=True)
    state = models.CharField(max_length=254, blank=True, null=True)
    gender = models.CharField(max_length=254, blank=True, null=True)
    type_of_house = models.CharField(max_length=254, blank=True, null=True)
    biogas_plant = models.CharField(max_length=254, blank=True, null=True)
    #longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uba_table'

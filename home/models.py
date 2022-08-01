# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class uba(models.Model):
   # id = models.CharField(primary_key=True, max_length=20)
    id = models.BigIntegerField(primary_key=True, max_length=20)
    #geom = models.GeometryField(blank=True, null=True)
    ward_no = models.BigIntegerField(blank=True, null=True)
    number_of_family_member = models.BigIntegerField(blank=True, null=True)
    own_house = models.CharField(max_length=254, blank=True, null=True)
    type_of_house = models.CharField(max_length=254, blank=True, null=True)
    toilet = models.CharField(max_length=254, blank=True, null=True)
    drainage_linked_to_house = models.CharField(max_length=254, blank=True, null=True)
    piped_Water_at_home = models.CharField(max_length=254, blank=True, null=True)
    electricity_connection_to_household = models.CharField(max_length=254, blank=True, null=True)
    schedule_filled_by_name = models.CharField(max_length=254, blank=True, null=True)
    block = models.CharField(max_length=254, blank=True, null=True)
    habitations = models.CharField(max_length=254, blank=True, null=True)
    gram_panchayat= models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    state = models.CharField(max_length=254, blank=True, null=True)
    gender = models.CharField(max_length=254, blank=True, null=True)
    type_of_house = models.CharField(max_length=254, blank=True, null=True)
    biogas_plant = models.CharField(max_length=254, blank=True, null=True)
    village = models.CharField(max_length=254, blank=True, null=True)
    #longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uba_table'

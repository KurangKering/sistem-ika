from django.db import models
from django.db.models.signals import pre_save
from data_uji.models import DataUji
# Create your models here.

class DataPengujian(models.Model):
	rules = models.TextField()
	cf_combine = models.FloatField()
	data_uji = models.OneToOneField(
        DataUji,
        on_delete=models.CASCADE,
        primary_key=True,
    )


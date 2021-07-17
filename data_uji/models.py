from django.db import models
from django.db.models.signals import pre_save
# Create your models here.

class DataUji(models.Model):
	nama_pasien = models.CharField(max_length=200, blank=True, null=True)
	age = models.FloatField(default=0)
	trestbps = models.FloatField(default=0)
	chol = models.FloatField(default=0)
	thalach = models.FloatField(default=0)
	oldpeak = models.FloatField(default=0)
	sex = models.FloatField(default=0)
	cp = models.FloatField(default=0)
	fbs = models.FloatField(default=0)
	restach = models.FloatField(default=0)
	exang = models.FloatField(default=0)
	slope = models.FloatField(default=0)
	ca = models.FloatField(default=0)
	thal = models.FloatField(default=0)
	target = models.IntegerField(default=0)


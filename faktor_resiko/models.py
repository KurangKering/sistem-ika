from django.db import models
# Create your models here.

class FaktorResiko(models.Model):
	faktor = models.CharField(max_length=200, blank=True, null=True)
	display_name = models.CharField(max_length=200, blank=True, null=True)


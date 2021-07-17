from django.db import models
# Create your models here.

class FaktorResiko(models.Model):
	faktor = max_length=odels.CharField(max_length=200, blank=True, null=True)
	display_name = models.CharField(max_length=200, blank=True, null=True)


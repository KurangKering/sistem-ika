from django import forms

class DataUjiForm(forms.Form):
	nama_pasien = forms.CharField()
	age = forms.FloatField()
	trestbps = forms.FloatField()
	chol = forms.FloatField()
	thalach = forms.FloatField()
	oldpeak = forms.FloatField()
	sex = forms.FloatField()
	cp = forms.FloatField()
	fbs = forms.FloatField()
	restach = forms.FloatField()
	exang = forms.FloatField()
	slope = forms.FloatField()
	ca = forms.FloatField()
	thal = forms.FloatField()
	target = forms.IntegerField()

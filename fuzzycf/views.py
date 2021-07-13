from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import numpy as np
from libraries.perhitungan import Perhitungan
# Create your views here.

def index(request):

	input_data = request.GET.get('input')
	x = eval(input_data)
	perhitungan = Perhitungan(x)
	perhitungan.mulai_perhitungan()
	nomor = [x for x in range(1,len(perhitungan.get_human_bobot()) +1)]

	context = {
		'cf_combine': perhitungan.get_cf_combine(),
		'input_data': perhitungan.get_input_data(),
		'nilai_cf': perhitungan.get_nilai_cf(),
		'nilai_fuzzy': perhitungan.get_nilai_fuzzy(),
		'nilai_prediket': perhitungan.get_nilai_prediket(),
		'nilai_rules': perhitungan.get_nilai_rules(),
		'human_rules': perhitungan.get_human_rules(),
		'human_bobot': perhitungan.get_human_bobot(),
		'rules_bobot': zip(nomor, perhitungan.get_human_rules(), perhitungan.get_human_bobot()),
		'z': perhitungan.get_z(),
	}
	return render(request, 'index.html', context)


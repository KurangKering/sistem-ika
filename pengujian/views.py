from django.shortcuts import render
from data_uji.models import DataUji
from utils.helper import context_response
from django.http import HttpResponse, JsonResponse
from libraries.perhitungan import Perhitungan
from .models import DataPengujian
from .forms import DataPengujianForm
from django.forms.models import model_to_dict

def index(request):
	pass

def detail(request):

    id_data_uji = request.POST.get('id')
    data_uji = DataUji.objects.get(pk=id_data_uji)
    data_pengujian = data_uji.datapengujian
    serial_data_uji = model_to_dict(data_uji)
    serial_data_pengujian = model_to_dict(data_pengujian)

    context = context_response(True, {'data_uji': serial_data_uji, 'data_pengujian': serial_data_pengujian})

    return JsonResponse(context, safe=False)

def pengujian_data_uji(request):
    data_uji_objects = DataUji.objects.all()
    daftar_data_uji = data_uji_objects.values_list('age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'sex', 'cp', 'fbs', 'restach', 'exang', 'slope', 'ca', 'thal')
    target_data_uji = data_uji_objects.values_list('target')

    data_uji_perhitungan = [list(x) for x in daftar_data_uji]
    for index_uji, data_uji in enumerate(data_uji_objects):
        perhitungan = Perhitungan(data_uji_perhitungan[index_uji])
        perhitungan.mulai_perhitungan()
        cf_combine = perhitungan.get_cf_combine()
        human_rules =  perhitungan.get_human_rules()
        data_uji.datapengujian = DataPengujian()
        data_uji.datapengujian.cf_combine = cf_combine
        data_uji.datapengujian.rules = human_rules
        data_uji.datapengujian.save()

    context = context_response(True, {})
    return JsonResponse(context, safe=False)

def pengujian_tunggal(request):
    form = DataPengujianForm(request.POST)
    if form.is_valid():
        post_data = form.cleaned_data
        post_dict = {
            'age' : post_data['age'],
            'trestbps' : post_data['trestbps'],
            'chol' : post_data['chol'],
            'thalach' : post_data['thalach'],
            'oldpeak' : post_data['oldpeak'],
            'sex' : post_data['sex'],
            'cp' : post_data['cp'],
            'fbs' : post_data['fbs'],
            'restach' : post_data['restach'],
            'exang' : post_data['exang'],
            'slope' : post_data['slope'],
            'ca' : post_data['ca'],
            'thal' : post_data['thal'],
            }

        post_list = [item for key, item in post_dict.items()]
        perhitungan = Perhitungan(post_list)
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
            'human_nilai': perhitungan.get_human_nilai(),
            'rules_nilai': list(zip(nomor, perhitungan.get_human_rules(), perhitungan.get_human_nilai())),
            'rules_bobot': list(zip(nomor, perhitungan.get_human_rules(), perhitungan.get_human_bobot())),
            'z': perhitungan.get_z(),
            }
    else:
        context = context_response(False, 'periksa inputan')

    context = context_response(True, context)
    return JsonResponse(context, safe=False)

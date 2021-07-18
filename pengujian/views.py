from django.shortcuts import render
from data_uji.models import DataUji
from utils.helper import context_response
from django.http import HttpResponse, JsonResponse
from libraries.perhitungan import Perhitungan
from .models import DataPengujian
from .forms import DataPengujianForm
from django.forms.models import model_to_dict
from utils.helper import set_kelas_klasifikasi
from django.views.decorators.csrf import csrf_exempt

def index(request):
	pass

@csrf_exempt
def detail(request):

    id_data_uji = request.POST.get('id')
    data_pengujian = DataPengujian.objects.get(data_uji_id=id_data_uji)
    serial_data_uji = model_to_dict(data_pengujian.data_uji)
    serial_data_pengujian = model_to_dict(data_pengujian)

    context = context_response(True, {'data_uji': serial_data_uji, 'data_pengujian': serial_data_pengujian})

    return JsonResponse(context, safe=False)

def index_pengujian_data_uji(request):

    data_pengujian = DataPengujian.objects.all()
    total_data_pengujian = DataPengujian.objects.count()
    total_benar = 0
    for data in data_pengujian:
        if (data.kelas == data.data_uji.target):
            total_benar = total_benar + 1

    total_salah = 0
    akurasi = 0
    if (total_data_pengujian > 0):
        total_salah = total_data_pengujian - total_benar
        akurasi = total_benar / total_data_pengujian * 100

    context = {
        'total_data': total_data_pengujian,
        'total_benar': total_benar,
        'total_salah': total_salah,
        'akurasi': round(akurasi,2)
    }
    context = context_response(True, context)
    return render(request, 'pengujian/index_pengujian_data_uji.html', context)

def index_pengujian_tunggal(request):

    return render(request, 'pengujian/index_pengujian_tunggal.html')

def pengujian_data_uji(request):
    data_uji_objects = DataUji.objects.all()
    daftar_data_uji = data_uji_objects.values_list('age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'sex', 'cp', 'fbs', 'restach', 'exang', 'slope', 'ca', 'thal')
    target_data_uji = data_uji_objects.values_list('target')

    data_uji_perhitungan = [list(x) for x in daftar_data_uji]
    list_data_pengujian = []
    total_benar = 0
    for index_uji, data_uji in enumerate(data_uji_objects):
        perhitungan = Perhitungan(data_uji_perhitungan[index_uji])
        perhitungan.mulai_perhitungan()
        cf_combine = perhitungan.get_cf_combine()
        human_rules =  perhitungan.get_human_rules()
        data_uji.datapengujian = DataPengujian()
        data_uji.datapengujian.cf_combine = cf_combine
        kelas = set_kelas_klasifikasi(cf_combine)
        data_uji.datapengujian.kelas = kelas
        data_uji.datapengujian.rules = human_rules
        list_data_pengujian.append(data_uji.datapengujian)
        if (kelas == data_uji.target):
            total_benar = total_benar + 1

    delete_old = DataPengujian.objects.all().delete()
    bulk_create = DataPengujian.objects.bulk_create(list_data_pengujian)

    total_data_pengujian = len(list_data_pengujian)
    total_salah = total_data_pengujian - total_benar
    akurasi = total_benar / total_data_pengujian * 100

    context = {
        'total_data': total_data_pengujian,
        'total_benar': total_benar,
        'total_salah': total_salah,
        'akurasi': round(akurasi,2)
    }
    context = context_response(True, context)
    return JsonResponse(context, safe=False)

@csrf_exempt
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

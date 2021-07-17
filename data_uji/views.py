from django.shortcuts import render
from utils.helper import context_response
from .models import DataUji
from .forms import DataUjiForm
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
import openpyxl
from itertools import islice
from django.db import connection


# Create your views here.

def index(request):


	return render(request, 'data_uji/index.html')

def detail(request):
    id_data_uji = request.POST.get('id')
    if (id_data_uji == None or id_data_uji == ''):
        context = context_response(False, 'id tidak boleh kosong')


    data_uji = DataUji.objects.get(pk=id_data_uji)
    serial = model_to_dict(data_uji)

    context = context_response(True, serial)

    return JsonResponse(context, safe=False)


def insert_or_update(request):

	id_data_uji = request.POST.get('id')

	if (id_data_uji == '' or id_data_uji == None):
		context = insert(request)
	else:
		context = update(request)

	return JsonResponse(context, safe=False)


def insert(request):
    form = DataUjiForm(request.POST)
    if form.is_valid():
        post_data = form.cleaned_data
        data_uji = DataUji()
        data_uji.nama_pasien = post_data['nama_pasien']
        data_uji.age = post_data['age']
        data_uji.trestbps = post_data['trestbps']
        data_uji.chol = post_data['chol']
        data_uji.thalach = post_data['thalach']
        data_uji.oldpeak = post_data['oldpeak']
        data_uji.sex = post_data['sex']
        data_uji.cp = post_data['cp']
        data_uji.fbs = post_data['fbs']
        data_uji.restach = post_data['restach']
        data_uji.exang = post_data['exang']
        data_uji.slope = post_data['slope']
        data_uji.ca = post_data['ca']
        data_uji.thal = post_data['thal']
        data_uji.target = post_data['target']
        data_uji.save()

        context = context_response(True, 'sukses menambah data uji')

    else:
        context = context_response(False, form.errors)

    return context


def update(request):
	form = DataUjiForm(request.POST)

	if form.is_valid():
		post_data = form.cleaned_data
		post_data = form.cleaned_data
		data_uji = DataUji.objects.get(pk=request.POST.get('id'))
		data_uji.nama_pasien = post_data['nama_pasien']
		data_uji.age = post_data['age']
		data_uji.trestbps = post_data['trestbps']
		data_uji.chol = post_data['chol']
		data_uji.thalach = post_data['thalach']
		data_uji.oldpeak = post_data['oldpeak']
		data_uji.sex = post_data['sex']
		data_uji.cp = post_data['cp']
		data_uji.fbs = post_data['fbs']
		data_uji.restach = post_data['restach']
		data_uji.exang = post_data['exang']
		data_uji.slope = post_data['slope']
		data_uji.ca = post_data['ca']
		data_uji.thal = post_data['thal']
		data_uji.target = post_data['target']
		data_uji.save()
		context = context_response(True, ['sukses merubah data uji'])

	else:
		context = context_response(False, form.errors)

	return context

def delete(request):
    id_data_uji = request.POST.get('id')
    data_uji = DataUji.objects.get(pk=id_data_uji)

    if (data_uji.delete()):
        context = context_response(True, 'sukses menghapus data uji')
    else:
        context = context_response(False, 'gagal menghapus data uji')

    return JsonResponse(context, safe=False)


def import_data(request):

	excel_file = request.FILES['excel_file']

	wb = openpyxl.load_workbook(excel_file)
	worksheet = wb['Sheet1']
	excel_data = []

	field_names = [
		'nama_pasien',
		'age',
		'trestbps',
		'chol',
		'thalach',
		'oldpeak',
		'sex',
		'cp',
		'fbs',
		'restach',
		'exang',
		'slope',
		'ca',
		'thal',
		'target'
		]

	for row in islice(worksheet.iter_rows(), 1, None):

		row_data = dict()
		for index in range(len(row)):
			row_data[field_names[index]] = str(row[index].value).strip()
			data_uji = DataUji(**row_data)
		excel_data.append(data_uji)



	if request.POST.get('hapus_seluruh_data') == 'on':
		DataUji.objects.all().delete()
		table_name = DataUji.objects.model._meta.db_table

		sql = ""

		if (connection.vendor == 'sqlite'):
			sql = "DELETE FROM SQLite_sequence WHERE name='{}';".format(table_name)
		elif (connection.vendor == 'postgresql'):

			sequence = f"{table_name}_id_seq"
			sql = "ALTER SEQUENCE IF EXISTS {} RESTART WITH 1;".format(sequence)


		with connection.cursor() as cursor:
			cursor.execute(sql)

	DataUji.objects.bulk_create(excel_data)
	total_data = len(DataUji.objects.all().values())
	context = context_response(True, {'total_data': total_data})
	return JsonResponse(context, safe=False)

#

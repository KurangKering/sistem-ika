from django.test import TestCase, Client
from data_uji.models import DataUji
from pprint import pprint
# Create your tests here.
#
#

class DataUjiViewTestCase(TestCase):

	def test_index(self):
		c = Client()
		response = c.get('/data-uji/index')
		pass

	def test_datatable(self):
		pass
	def test_detail(self):
		pass

	def test_insert_or_update(self):

		pass

	def test_insert(self):
		post_data = {
			'nama_pasien': '0.5',
			'age': '0.5',
			'trestbps': '0.5',
			'chol': '0.5',
			'thalach': '0.5',
			'oldpeak': '0.5',
			'sex': '0.5',
			'cp': '0.5',
			'fbs': '0.5',
			'restach': '0.5',
			'exang': '0.5',
			'slope': '0.5',
			'ca': '0.5',
			'thal': '0.5',
			'target': '1',
		}

		c = Client()
		response = c.post('/data-uji/insert_or_update', post_data)


	def test_update(self):
		post_data = {
			'nama_pasien': '0.5',
			'age': '0.5',
			'trestbps': '0.5',
			'chol': '0.5',
			'thalach': '0.5',
			'oldpeak': '0.5',
			'sex': '0.5',
			'cp': '0.5',
			'fbs': '0.5',
			'restach': '0.5',
			'exang': '0.5',
			'slope': '0.5',
			'ca': '0.5',
			'thal': '0.5',
			'target': '1',
		}

		c = Client()
		response = c.post('/data-uji/insert_or_update', post_data)

		post_data = {
			'id': '1',
			'nama_pasien': '0.1',
			'age': '0.2',
			'trestbps': '0.3',
			'chol': '0.4',
			'thalach': '0.5',
			'oldpeak': '0.6',
			'sex': '0.7',
			'cp': '0.8',
			'fbs': '0.9',
			'restach': '0.10',
			'exang': '0.11',
			'slope': '0.12',
			'ca': '0.13',
			'thal': '0.14',
			'target': '2',
		}

		c = Client()
		response = c.post('/data-uji/insert_or_update', post_data)

	def test_delete(self):
		post_data = {
			'nama_pasien': '0.5',
			'age': '0.5',
			'trestbps': '0.5',
			'chol': '0.5',
			'thalach': '0.5',
			'oldpeak': '0.5',
			'sex': '0.5',
			'cp': '0.5',
			'fbs': '0.5',
			'restach': '0.5',
			'exang': '0.5',
			'slope': '0.5',
			'ca': '0.5',
			'thal': '0.5',
			'target': '1',
		}

		c = Client()
		response = c.post('/data-uji/insert_or_update', post_data)

		print(DataUji.objects.all().values())
		post_data = {
			'id': 1
		}

		c = Client()
		response = c.post('/data-uji/delete', post_data)


	def tests_import_data(self):
		c = Client()
		response = None
		with open('C:/Users/Ya/Downloads/data-import-ika.xlsx', 'rb') as fp:
			response = c.post('/data-uji/import_data', {'excel_file' : fp, 'hapus_seluruh_data': 'on'})
			print(response)

		data_uji = DataUji.objects.all()
		print(data_uji)


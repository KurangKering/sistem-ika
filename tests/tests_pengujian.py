from django.test import TestCase, Client
from data_uji.models import DataUji
from pprint import pprint
# Create your tests here.
#
#

class PengujianDataUjiViewTestCase(TestCase):
	def test_detail(self):
		post_data = {
			'id': 1
		}

		c = Client()
		response = c.post('/pengujian/detail', post_data)
		print(response.content)

		
	def test_pengujian_data_uji(self):
		c = Client()
		response = c.get('/pengujian/pengujian_data_uji')
		print(response.content)















	def test_pengujian_tunggal(self):
		c = Client()
		post_data = {
			'age': '41',
			'trestbps': '130',
			'chol': '204',
			'thalach': '172',
			'oldpeak': '1.4',
			'sex': '0',
			'cp': '1',
			'fbs': '0',
			'restach': '0',
			'exang': '0',
			'slope': '2',
			'ca': '0',
			'thal': '2',
		}
		response = c.post('/pengujian/pengujian_tunggal', post_data)
		print(response.content)



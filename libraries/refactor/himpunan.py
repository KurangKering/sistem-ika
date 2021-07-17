class Himpunan(BaseHimpunan):

	def __init__(nama, bobot, mf):
		self._nama = nama
		self._bobot = bobot
		self._mf = mf
		self._nilai = None


	def hitung(self, nilai):
		self._nilai = mf.calculate(nilai)


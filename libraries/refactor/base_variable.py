class BaseVariable(object):

		
	def calculate(self, nilai):
		self._daftar_nilai = []
		for himpunan in range(self._daftar_himpunan):
			himpunan.hitung(nilai)
			self._daftar_nilai.append(nilai)

    def get_identitas(self):
        return self._identitas
    
    def get_daftar_himpunan(self):
        return self._daftar_himpunan

    def get_himpunan(self, index):
    	return self._daftar_himpunan[index]



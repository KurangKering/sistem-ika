from .base import *

class MF_Trestbps(BaseMF, ForFuzzyVariable):
    
    _identitas = "TRESTBPS"
    _bobot = [0.3, 0.5, 0.7, 0.9]
    _himpunan = ['rendah', 'sedang', 'tinggi', 'sangat tinggi']
    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        _rendah = fuzz.trapmf(x, [0, 0, 127, 134])
        _sedang = fuzz.trapmf(x, [127, 134, 142, 153])
        _tinggi = fuzz.trapmf(x, [142, 153, 154, 172])

        _replaced_x = np.array(list(map(lambda y : y if y <= 172 else 172, x)))

        _sangat_tinggi = fuzz.trapmf(_replaced_x, [154, 172, 172, 172])
        
        _merged = np.vstack((_rendah, _sedang, _tinggi, _sangat_tinggi))
        transposed = _merged.T

        if (isinstance(inputan, np.ndarray) is False):
            return transposed[0]
        return transposed
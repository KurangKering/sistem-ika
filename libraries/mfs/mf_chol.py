from .base import *

class MF_Chol(BaseMF, ForFuzzyVariable):
    
    _identitas = "CHOL"
    _bobot = [0.5, 0.7, 0.8, 0.9]
    _himpunan = ['rendah', 'sedang', 'tinggi', 'sangat tinggi']
    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        _rendah = fuzz.trapmf(x, [0, 0, 188, 197])
        _sedang = fuzz.trapmf(x, [188, 197, 217, 250])
        _tinggi = fuzz.trapmf(x, [217, 250, 281, 307])

        _replaced_x = np.array(list(map(lambda y : y if y <= 307 else 307, x)))

        _sangat_tinggi = fuzz.trapmf(_replaced_x, [281, 307, 307, 307])
        
        _merged = np.vstack((_rendah, _sedang, _tinggi, _sangat_tinggi))
        transposed = _merged.T

        if (isinstance(inputan, np.ndarray) is False):
            return transposed[0]
        return transposed
        
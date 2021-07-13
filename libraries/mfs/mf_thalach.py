from .base import *

class MF_Thalach(BaseMF, ForFuzzyVariable):
    
    _identitas = "THALACH"
    _bobot = [0.3, 0.5, 0.7]
    _himpunan = ['rendah', 'sedang', 'tinggi']
    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        _rendah = fuzz.trapmf(x, [0, 0, 111, 141])
        _sedang = fuzz.trapmf(x, [111, 141, 152, 194])

        _replaced_x = np.array(list(map(lambda y : y if y <= 194 else 194, x)))
        _tinggi = fuzz.trapmf(_replaced_x, [152, 194, 194, 194])

        _merged = np.vstack((_rendah, _sedang, _tinggi))
        transposed = _merged.T

        if (isinstance(inputan, np.ndarray) is False):
            return transposed[0]
        return transposed
        

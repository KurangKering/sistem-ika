from .base import *

class MF_Oldpeak(BaseMF, ForFuzzyVariable):
    
    _identitas = "OLDPEAK"
    _bobot = [0.5, 0.5, 0.5]
    _himpunan = ['rendah', 'beresiko', 'buruk']
    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        _rendah = fuzz.trapmf(x, [0, 0, 1.5, 2])
        _sedang = fuzz.trapmf(x, [1.5, 2, 2.55, 4.2])

        _replaced_x = np.array(list(map(lambda y : y if y <= 4.2 else 4.2, x)))
        _tinggi = fuzz.trapmf(_replaced_x, [2.55, 4.2, 4.2, 4.2])

        _merged = np.vstack((_rendah, _sedang, _tinggi))
        transposed = _merged.T

        if (isinstance(inputan, np.ndarray) is False):
            return transposed[0]
        return transposed
        

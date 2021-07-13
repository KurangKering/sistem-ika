from .base import *

class MF_Age(BaseMF, ForFuzzyVariable):
    
    _identitas = "AGE"
    _bobot = [0.3, 0.5, 0.7, 0.8]
    _himpunan = ['muda', 'agak tua', 'tua', 'sangat tua']
    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            
        _muda = fuzz.trapmf(x, [0, 0, 33, 38])
        _agak_tua = fuzz.trapmf(x, [33, 38, 40, 45])
        _tua = fuzz.trapmf(x, [40, 45, 52, 58])

        _replaced_x = np.array(list(map(lambda y : y if y <= 58 else 58, x)))

        _sangat_tua = fuzz.trapmf(_replaced_x, [52, 58, 58, 58])
        
        _merged = np.vstack((_muda, _agak_tua, _tua, _sangat_tua))
        transposed = _merged.T
        
        if (isinstance(inputan, np.ndarray) is False):
            return transposed[0]
        return transposed
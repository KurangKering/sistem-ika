from .base import *

class MF_Fbs(BaseMF):
    
    _identitas = "FBS"
    _bobot = [0.4, 0.8]
    _himpunan = ['tidak', 'ya']

    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        new_x = np.array(list(map(lambda y : 0 if y <= 120 else 1, x)))

        if (isinstance(inputan, np.ndarray) is False):
            return new_x

        return new_x[:, None]
        
    @staticmethod
    def get_index(x):
        if any(i > 1 for i in x) or any(i < 0 for i in x):
            raise ValueError('nilai berada diantara 0 dan 1')

        if (x.ndim <= 1):
            return list(map(lambda y: y, x))
        
        indexes = []
        for i in range(len(x)):
            matching = x[i]
            indexes.append(matching.tolist())
        return indexes
    
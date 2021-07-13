from .base import *

class MF_Ca(BaseMF):
    
    _identitas = "CA"
    _bobot = [0.5, 0.5, 0.5, 0.5]
    _himpunan = ['ca1', 'ca2', 'ca3', 'ca4']

    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        if any(i > 3 for i in x) or any(i < 0 for i in x):
            raise ValueError('nilai berada diantara 0 dan 3')

        if (isinstance(inputan, np.ndarray) is False):
            return x


        return x[:, None]
    
    
    @staticmethod
    def get_index(x):
        if any(i > 3 for i in x) or any(i < 0 for i in x):
            raise ValueError('nilai berada diantara 0 dan 3')

        
        if (x.ndim <= 1):
            return list(map(lambda y: y, x))
        
        indexes = []
        for i in range(len(x)):
            matching = x[i]
            indexes.append(matching.tolist())
        return indexes



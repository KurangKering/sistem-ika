from .base import *

class MF_Sex(BaseMF):
    
    _identitas = "SEX"
    _bobot = [0.4, 0.5]
    _himpunan = ['perempuan', 'laki-laki']
    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        if any(i > 1 for i in x) or any(i < 0 for i in x):
            raise ValueError('nilai berada diantara 0 dan 1')


        if (isinstance(inputan, np.ndarray) is False):
            return x
        return x[:, None]
    
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
    
from .base import *

class MF_Restach(BaseMF):
    
    _identitas = "RESTACH"
    _bobot = [0.2, 0.9, 0.9]
    _himpunan = ['normal', 'ST-T wave abnormality', 'hypertrophy']

    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        if any(i > 2 for i in x) or any(i < 0 for i in x):
            raise ValueError('nilai berada diantara 0 dan 2')

        if (isinstance(inputan, np.ndarray) is False):
            return x


        return x[:, None]
    
         
    @staticmethod
    def get_index(x):
        if any(i > 2 for i in x) or any(i < 0 for i in x):
            raise ValueError('nilai berada diantara 0 dan 2')

        if (x.ndim <= 1):
            return list(map(lambda y: y, x))
        
        indexes = []
        for i in range(len(x)):
            matching = x[i]
            indexes.append(matching.tolist())
        return indexes


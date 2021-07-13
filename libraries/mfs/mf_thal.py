from .base import *

class MF_Thal(BaseMF):
    
    _identitas = "THAL"
    _himpunan = ['normal', 'fixed defect', 'reversible defect']
    _bobot = [0.3, 0.7, 0.8]

    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        new_x = np.array(list(map(lambda y : 0 if y < 5.5 else 2 if y > 6.2 else 1, x)))

        if (isinstance(inputan, np.ndarray) is False):
            return new_x

        return new_x[:, None]


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


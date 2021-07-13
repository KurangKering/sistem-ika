from .base import *

class MF_Slope(BaseMF):
    
    _identitas = "SLOPE"
    _bobot = [0.5, 0.5,0.5]
    _himpunan = ['upsloping', 'flat', 'downsloping']

    
    @staticmethod
    def calculate(inputan):
        if (isinstance(inputan, np.ndarray) is False):
            x = np.array([inputan])
        else:
            x = inputan.copy()
            

        if any(i > 3 for i in x) or any(i < 1 for i in x):
            raise ValueError('nilai berada diantara 1 dan 3')
        
        new_x = np.array(list(map(lambda y: y - 1, x)))

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

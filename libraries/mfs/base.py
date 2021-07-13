import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from numpy import unravel_index
import itertools

from abc import ABC, abstractmethod

class BaseMF:
    
    
    @classmethod
    def get_identitas(cls):
        return cls._identitas
    
    @classmethod
    def get_himpunan(cls, index):
        return cls._himpunan[index]
    
    @classmethod
    def get_bobot(cls, index):
        return cls._bobot[index]

    @abstractmethod
    def calculate(inputan):
        pass

class ForFuzzyVariable:
    
    @staticmethod
    def get_index(x):
        if (x.ndim <= 1):
            return np.argwhere(x > 0).flatten().tolist()

        indexes = []
        for i in range(len(x)):
            matching = np.argwhere(x[i] > 0).flatten()
            indexes.append(matching.tolist())
        return indexes
    
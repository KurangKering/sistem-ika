from libraries.mfs import *
import numpy as np
class Perhitungan:

    _algs = [MF_Age, MF_Trestbps, MF_Chol, MF_Thalach, MF_Oldpeak, MF_Sex, MF_Cp, MF_Fbs, MF_Restach, MF_Exang, MF_Slope, MF_Ca, MF_Thal]


    def __init__(self, input_data):
        self.input_data = input_data.copy()
        if (isinstance(input_data, np.ndarray) is False):
            self.input_data = np.array(input_data)

        self.rules = None

    def mulai_perhitungan(self):
        nilai = self._hitung_nilai_fuzzy(self.input_data)
        rules = self._hitung_rules(nilai)
        nilai_target_rules = self._hitung_nilai_rules(rules)

        nilai_prediket = self._hitung_nilai_prediket(nilai, rules)
        nilai_z = self._hitung_nilai_z(nilai_prediket, nilai_target_rules)

        nilai_cf = self._hitung_nilai_cf(nilai_z, nilai_target_rules)


        self._hitung_nilai_combine(nilai_cf)
        

    def _hitung_nilai_fuzzy(self, variables):
        arr = self.input_data.copy()
        self.nilai_fuzzy = [Perhitungan._algs[x].calculate(arr[x]) for x in range(len(arr))]
        return self.nilai_fuzzy
    
    

    def _hitung_rules(self, nilai_fuzzy):
        kombinasi = [[int(y) for y in Perhitungan._algs[x].get_index(nilai_fuzzy[x])] for x in range(len(nilai_fuzzy))]
        self.kombinasi = kombinasi

        self.rules = list(itertools.product(*kombinasi))
        return self.rules

    def _hitung_nilai_rules(self, rules):

        nilai_rules = []
        for i in range(len(rules)):
            sigma_ = sum([Perhitungan._algs[x].get_bobot(rules[i][x]) for x in range(len(rules[i]))])
            nilai = sigma_ / len(rules[i])
            nilai_rules.append(nilai)

        self.nilai_rules = nilai_rules
        return nilai_rules

    def _hitung_nilai_prediket(self, nilai, rules):

        list_prediket = []
        for i in range(len(rules)):
            v_fuzzy = [nilai[x][rules[i][x]] for x in range(5)]
            v_nonfuzzy = [nilai[x][0] for x in range(5,13)]
            max_non = max(v_nonfuzzy)
            prediket = min(min(v_fuzzy),max_non)
            list_prediket.append(prediket)

        self.nilai_prediket = list_prediket
        return list_prediket

    def _hitung_nilai_z(self, nilai_prediket, nilai_target):
        sigma_target = sum(nilai_target)
        sigma_prediket = sum(nilai_prediket)
        sigma_prediket_kali_target = sum(x * y for x,y in zip(nilai_prediket, nilai_target))

        z = sigma_prediket_kali_target / sigma_prediket

        self.z = z
        return z

    def _hitung_nilai_cf(self, z, nilai_target):
        self.nilai_cf =  [z * x for x in nilai_target]
        return self.nilai_cf

    def _hitung_nilai_combine(self, nilai_cf):
        asal = 0
        for i in range(len(nilai_cf)):
            penambah = 0
            if 0 <= i+1 < len(nilai_cf):
                penambah = nilai_cf[i+1]

            if i == 0:
                asal = nilai_cf[i]

            asal =  asal + penambah * (1 - asal)
        self.cf_combine = asal
        return asal


    def get_human_rules(self):
        human_rules = []
        for i in range(len(self.rules)):
            human = [f'{self._algs[x].get_identitas()} {self._algs[x].get_himpunan(self.rules[i][x])}' for x in range(len(self.rules[i]))]
            string_human = ' & '.join(human)
            string_human = f'IF {string_human} = {round(self.nilai_rules[i],4)}'
            human_rules.append(string_human)
        
        return human_rules
    
    def get_human_bobot(self):
        human_bobot = []
        for i in range(len(self.rules)):
            human = [f'{self._algs[x].get_identitas()} {self._algs[x].get_bobot(self.rules[i][x])}' for x in range(len(self.rules[i]))]
            string_human = ' & '.join(human)
            string_human = f'IF {string_human} = {round(self.nilai_rules[i],4)}'
            human_bobot.append(string_human)
        
        return human_bobot

    def get_cf_combine(self):
        return self.cf_combine

    def get_input_data(self):
        return self.input_data.copy().tolist()

    def get_kombinasi(self):
        return self.kombinasi

    def get_nilai_cf(self):
        return self.nilai_cf

    def get_nilai_fuzzy(self):
        return [self.nilai_fuzzy[x].tolist() for x in range(len(self.nilai_fuzzy))]

    def get_nilai_prediket(self):
        return self.nilai_prediket

    def get_nilai_rules(self):
        return self.nilai_rules

    def get_rules(self):
        return self.rules

    def get_z(self):
        return self.z
        
        

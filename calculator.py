# calculator.py
import math
from config import WORK_SHIFTS

def calculate_equipment(data):
    """
    Принимает словарь с исходными данными.
    Возвращает словарь с результатами расчётов.
    """
    # 1. Производительность линии пельменей
    P_tlp = data["Q_sut"] / (WORK_SHIFTS * data["t"])
    
    # 2. Количество пельменных автоматов
    n_pa = math.ceil(P_tlp / data["p_pa"])
    
    # 3. Производительность линии теста
    P_tlt = (data["a_t"] * P_tlp) / 100
    
    # 4. Количество тестомесильных машин
    n_tm = math.ceil(P_tlt / data["p_tm"])
    
    # 5. Производительность линии фарша
    a_f = 100 - data["a_t"]
    P_tlf = (a_f * P_tlp) / 100
    
    # 6. Количество куттеров
    n_k = math.ceil(P_tlf / data["p_k"])
    
    return {
        "n_pa": n_pa,
        "n_tm": n_tm,
        "n_k": n_k,
        "P_tlp": P_tlp,
        "P_tlt": P_tlt,
        "P_tlf": P_tlf
    }
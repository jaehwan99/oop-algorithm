from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Dict

def get_terms_dict(terms:str) -> Dict:
    dict = {}
    for ele in list(terms):
        key, value = ele.split(' ')
        dict[key] = value
    return dict

def get_today_int(today:str) -> int:
    # date_format = "%Y.%m.%d"
    d = 28
    
    Y_format = 12 * d
    m_format = d
    year, month, day = today.split('.')
    
    return (int(year) * Y_format) + (int(month) * m_format) + int(day)

def get_convert_privacy_terms(privacy_date : int, term : int):
    d = 28
    return int(privacy_date) + int((term * d))

def solution(today, terms, privacies):
    answer = []
    
    terms_dict = get_terms_dict(terms)
    today_date = get_today_int(today)

    for idx, ele in enumerate(privacies) :
        privacy_date, terms = ele.split(' ')
        
        compare = get_convert_privacy_terms(get_today_int(privacy_date), int(terms_dict[terms]))
        
        if today_date >= compare:
            answer.append(idx+1)
            
    return answer

if __name__ == '__main__':
    assert [1, 3] == solution(today="2022.05.19"
                          , terms=["A 6", "B 12", "C 3"]
                          , privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
                          )

    assert [1,4,5] == solution(today="2020.01.01"
                               , terms=["Z 3", "D 5"]
                               , privacies=["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
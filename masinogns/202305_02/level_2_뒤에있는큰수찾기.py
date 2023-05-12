from typing import List

"""
global answer
answer = []

def recursive(param_list:List):
    checker = param_list.pop(0)
    
    append_value = -1
    flag = False
    for n in param_list:
        if checker < n:
            flag = True
            append_value = n
            answer.append(append_value)
            break
    
    if flag is False:
        answer.append(append_value)
        
    return recursive(param_list) if len(param_list) > 0 else 0

def solution(numbers:List) -> List:
    recursive(numbers)
    return answer
"""


def solution(numbers:List) -> List:
    answer = []
    return answer

if __name__ == '__main__':
    assert [3, 5, 5, -1] == solution(numbers=[2, 3, 3, 5])
    # assert [-1, 5, 6, 6, -1, -1] == solution(numbers=[9, 1, 5, 3, 6, 2])
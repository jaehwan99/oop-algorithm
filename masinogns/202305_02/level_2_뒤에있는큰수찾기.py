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

""" 시간초과 , acc : 56%, list.pop(0)의 시간복잡도 O(n)임.
def solution(numbers:List):
    answer = []
    
    checker =  None
    for i in range(len(numbers)):
        checker = numbers.pop(0)
        # print(i, checker, numbers)

        ans = None
        for n in numbers:
            if checker < n:
                ans = n 
                break
            else:
                ans = -1 
        # case list is empty 
        if ans is None:
            ans = -1
            
        answer.append(ans)
 
    # print(answer)
    return answer
"""


def solution(numbers: List):
    # 값 인덱스 접근을 위한 초기화 
    answer = [-1]  * len(numbers)
    stack = []
    
    for index, n in enumerate(numbers):
        # print(index, n, stack, numbers)
        
        # 리스트가 비어있으면 False, 값이 하나라도 있으면 True
        # numbers[stack[-1]]은 처음에 진행할 수 없어서 stack 조건을 함께 넣음 
        while stack and n > numbers[stack[-1]]:
            # print(":: ", n, numbers[stack[-1]], stack, numbers)
            answer[stack.pop()] = n

        stack.append(index)

    return answer

if __name__ == '__main__':
    assert [3, 5, 5, -1] == solution(numbers=[2, 3, 3, 5])
    assert [-1, 5, 6, 6, -1, -1] == solution(numbers=[9, 1, 5, 3, 6, 2])


''' accuracy : 93.3

'''
from typing import List
from collections import deque

def same_result_between_two_queue(queue1:List, queue2:List):
    count = 0
    
    total_queue_1 = sum(queue1)
    total_queue_2 = sum(queue2)
    
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    
    while True:
        if total_queue_1 > total_queue_2 :
            n = deque1.popleft()
            deque2.append(n)
            
            total_queue_1 -= n
            total_queue_2 += n
            
            count +=1
            # print('count : ', count, ' : ', queue1, queue2, total_queue_1, total_queue_2)
        elif total_queue_1 < total_queue_2 :
            n = deque2.popleft()
            deque1.append(n)
            
            total_queue_2 -= n
            total_queue_1 += n
            
            count +=1
            # print('count : ', count, ' : ', queue1, queue2, total_queue_1, total_queue_2)
            
        if (len(deque2) == 0 or len(deque2) == 0):
            count = -1
            break
               
        if (total_queue_1 == (total_queue_1+total_queue_2)/2):
            break

    return count
    
def solution(queue1:List, queue2:List):
    answer = -2
    
    answer = same_result_between_two_queue(queue1, queue2)
    
    return answer

if __name__ == '__main__':
    assert 2 == solution(queue1=[3, 2, 7, 2], queue2=[4, 6, 5, 1])
    
    assert 7 == solution(queue1=[1, 2, 1, 2], queue2=[1, 10, 1, 2])
    
    assert -1 == solution(queue1=[1, 1], queue2=[1, 5])
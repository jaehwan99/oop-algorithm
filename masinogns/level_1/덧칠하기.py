''' WAY 1 ) Fail
def solution(n, m, section):
    answer = 0
    
    max_loop_count = round(n/m)
    loop_section = section.copy()
    
    for loop in range(max_loop_count):
        rolling_min = loop_section[loop]
        rolling_max = (loop_section[loop] + m)
        
        for i in section:
            if (rolling_min <= i and i < rolling_max):
                print(loop, rolling_min, i, rolling_max)
                section.remove(i)
                answer += 1
        
    return answer
'''

def solution(n, m, section):
    answer = 0
    
    roller_max_length = 0
    
    for value in section:
        if value < roller_max_length:
            continue
        
        roller_max_length = value + m
        answer += 1
    
    return answer

if __name__ == '__main__':
    assert 2 == solution(n=8, m=4, section=[2,3,6])
    assert 1 == solution(n=5, m=4, section=[1,3])
    assert 4 == solution(n=4, m=1, section=[1,2,3,4])
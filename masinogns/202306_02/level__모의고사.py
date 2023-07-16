
def make_answer_list(answer):
    max_answer_limit = 10000
    return answer * int(max_answer_limit/len(answer))

def solution(answers):
    answer = {'1':0, '2':0, '3':0}
    
    human_one = [1, 2, 3, 4, 5]
    human_two = [2, 1, 2, 3, 2, 4, 2, 5]
    human_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    list_answers = make_answer_list(answers)
    list_one = make_answer_list(human_one)
    list_two = make_answer_list(human_two)
    list_three = make_answer_list(human_three)
    for ele, one, two, three in zip(list_answers, list_one, list_two, list_three):
        if ele == one:
            answer['1'] += 1
        
        if ele == two:
            answer['2'] += 1
        
        if ele == three:
            answer['3'] += 1
    
    print(answer, list(reversed(sorted(answer.items(), key=lambda item: item[1]))))
    
    return answer


if __name__ == '__main__':
    # params = [1,2,3,4,5]
    # assert [1] == solution(answers=params)
    
    params = [1,3,2,4,2]
    assert [1,2,3] == solution(answers=params)
def compare_two_element(first, last):
    if first[1] >= last[1]:
        return first[0]
    else:
        return last[0]

def solution(survey, choices):
    answer = ''
    metric_board = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    dict_choise_board = {1:(0,3),2:(0,2),3:(0,1),4:(0,0),5:(1,1),6:(1,2),7:(1,3)}
    
    for surv, choice in list(zip(survey, choices)):
        surv_index, surv_num = dict_choise_board[choice]
        metric_board[surv[surv_index]] = metric_board.get(surv[surv_index]) + surv_num
        
    metric_board = list(metric_board.items())
    
    for r in range(0, int(len(metric_board) / 2)):
        answer += compare_two_element(metric_board[int(2*r)], metric_board[int(2*r + 1)])
    return answer


if __name__ == '__main__':
    assert "TCMA" == solution(survey=["AN", "CF", "MJ", "RT", "NA"], choices=[5, 3, 2, 7, 5])
    assert "RCJA" == solution(survey=["TR", "RT", "TR"], choices=[7, 1, 3])
    
    '''
    2023-05-31 success
    '''
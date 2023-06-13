def solution(id_list, report, k):
    answer = {}
    report_info = {}
    # report_log = []
    
    for id in id_list:
        report_info[id] = {'count' : 0, 'user' : []}
        answer[id] = 0
        
    # create report info / log
    for r in report:
        reporting_user, reported_user = r.split(' ')
        
        # report_log.append({'reporting_user':reporting_user, 'reported_user':reported_user})
        if reporting_user not in report_info[reported_user]['user']:
            report_info[reported_user]['count'] += 1
            report_info[reported_user]['user'].append(reporting_user)
    
    # check report target user / mail send target
    for reported_user, reported_info in report_info.items():
        # print('bb : ', reported_user, reported_info)
        
        if reported_info['count'] >= k:
            target_set = set(reported_info['user'])
            # print('aa : ',reported_user, target_set, type(target_set))
            
            for target in target_set:
                answer[target] += 1
            
    answer = [value for value in answer.values()]
    return answer



if __name__ == '__main__':
    assert [2,1,1,0] == solution(id_list=["muzi", "frodo", "apeach", "neo"],report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], k=2)
    assert [0,0] == solution(id_list=["con", "ryan"],report=["ryan con", "ryan con", "ryan con", "ryan con"], k=3)
    
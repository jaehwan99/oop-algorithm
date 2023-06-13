def add_array_list(arr1, arr2):
    array = []        
    for element in list(zip(arr1, arr2)):
        array.append(sum(element))
    return array

def solution(arr1, arr2):
    answer = []
    
    for number in range(len(arr1)):
        answer.append(add_array_list(arr1[number], arr2[number]))
    
    return answer

if __name__ == '__main__':
    assert [[4,6],[7,9]] == solution(arr1=[[1,2],[2,3]], arr2=[[3,4],[5,6]])
    assert [[4],[6]] == solution(arr1=[[1],[2]], arr2=[[3],[4]])
    
    '''
    
    '''
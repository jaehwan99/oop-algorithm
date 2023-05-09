def get_alphabet_dict(skip:str):
    '''
    아스키코드 : 97(a) ~ 122(z)
    chr(97) = a
    ord('a') = 97
    '''
    alpavet_char, alpavet_no = {}, {}
    ascii_number_a = 97
    ascii_number_z = 122
    no = 0
    
    skip_list = list(skip)
    
    for idx in range(ascii_number_a, ascii_number_z+1):
        char = chr(idx)
        if char not in skip_list:
            alpavet_char[char] = no
            alpavet_no[no] = char
            
            no += 1
        
    return {
        'char' : alpavet_char, 'no' : alpavet_no
    }

def solution(s, skip, index):
    answer = ''
    
    alphabet = get_alphabet_dict(skip=skip)
    
    length = len(alphabet['no'])
    for st in list(s):
        answer += alphabet['no'][(alphabet['char'][st] + index)%(length)]
    
    return answer

if __name__ == '__main__':
    assert "happy" == solution(s="aukks",skip="wbqd", index=5)
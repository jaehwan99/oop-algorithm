def match_word(token):    
    prefix = {"z" : {("zero",4),}, "o":{("one",3)}, "t":{("two",3), ("three",5)}
              , "f":{("four",4),("five",4)}, "s":{("six",3),("seven",5)},"e":{("eight",5)},"n":{("nine",4)}}

    return prefix[token] if prefix.get(token) is not None else None

def solution(s):
    answer = 0
    keyword = {"zero":0,"one":1,"two":2,"three":3,"four":4,
               "five":5,"six":6,"seven":7,"eight":8,"nine":9}
    
    value, value_index, string_index = 0, 1, 0
    import time
    while True:
        matching_list = match_word(s[string_index])
        
        if matching_list is None:
            string_index += 1
            continue
        
        print(matching_list)
        for match in matching_list:
            print(matching_list, string_index, value_index, match[value_index], match, s[string_index:(string_index+match[value_index])])
            if match[value] == s[string_index:(string_index+match[value_index])]:
                string_index += match[value_index] - 1
    
        
        time.sleep(3)
        
    
    return answer

if __name__ == '__main__':
    assert 1478 == solution(s="one4seveneight")
    
    

def solution(keymap, targets):
    answer = []
    
    keymap_dict = {}
    
    for idx in range(len(keymap)):
        # keymap_dict initialize 
        for index, key in enumerate(keymap[idx]):
            if (not keymap_dict.get(key) is None) and (keymap_dict.get(key)[1] < index+1):
                continue
            
            # idx : 0 is keymap index / idx : 1 is minimum call count
            keymap_dict[key] = (idx, index+1)
    
    for target in targets:
        counter = 0
        # exception 처리가 key point
        try:
            for key in target:
                counter += keymap_dict[key][1]    
        except KeyError:
            counter = -1
        finally:
            answer.append(counter)

    return answer


if __name__ == '__main__':
    assert [9, 4] == solution(keymap=["ABACD", "BCEFD"],targets=["ABCD","AABB"])
    assert [-1] == solution(keymap=["AA"],targets=["B"])
    assert [4, 6] == solution(keymap=["AGZ", "BSSS"],targets=["ASA","BGZ"])
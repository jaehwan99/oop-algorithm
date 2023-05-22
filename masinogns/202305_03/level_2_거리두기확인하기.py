'''
코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

- 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
- 거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.
- 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

places의 행 길이(대기실 개수) = 5
places의 각 행은 하나의 대기실 구조를 나타냅니다.
places의 열 길이(대기실 세로 길이) = 5
places의 원소는 P,O,X로 이루어진 문자열입니다.
places 원소의 길이(대기실 가로 길이) = 5
P는 응시자가 앉아있는 자리를 의미합니다.
O는 빈 테이블을 의미합니다.
X는 파티션을 의미합니다.
입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다

두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다

'''
import numpy as np

def solution(places):
    answer = []
    array = np.array(places[0])
    
    print(array[0][4], array[1][2], array[2][1], array)
    
    return answer

if __name__ == '__main__':
    assert [] == solution(places=[
                            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
                            , ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
                            , ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]
                            , ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]
                            , ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
                            ])
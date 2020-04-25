# Code Festival - Python Practice 076
# Author : ㄱㄱㅊ
# Title : Safe Land
# Date : 20-04-25

n = int(input())

for tcn in range(n):                    # test case number

    a, b = map(int, input().split())    # a = 도시의 크기
    mines = []                          # b = 수색 가능 범위
    max_num = 0
    for i in range(a):                  
        mines.append(list(map(int, input().split())))

    # 테스트
    '''
    a, b = 5, 3
    max_num = 0
    mines = [[1, 0, 0, 1, 0],
             [0, 1, 0, 0, 1],
             [0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0]]
    '''

    # 최대값 찾기
    rep = (a + 1) - b                   # repeat
    for i in range(rep):
        for j in range(rep):
            mine_num = (sum(mines[ i ][j:j+3]) +
                        sum(mines[i+1][j:j+3]) +
                        sum(mines[i+2][j:j+3]))

            if mine_num > max_num:
                max_num = mine_num
    
    

print(max_num)

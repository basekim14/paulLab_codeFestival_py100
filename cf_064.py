# Code Festival - Python Practice 064
# Author : ㄱㄱㅊ
# Title : Strange Elevator
# Date : 20-04-19

def check_quantity(N):
    if N % 7 == 0:
        return N // 7
    
    result = []
    i = 0
    while i * 7 < N:
        M = N - (i * 7)
        if M % 3 == 0:
            result.append((i, M // 3))

        i += 1

    if result:
        return min([result[k][0] + result[k][1] for k in range(len(result))])
    else:
        return -1

N = int(input())
print(check_quantity(N))



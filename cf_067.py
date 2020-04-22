# Code Festival - Python Practice 067
# Author : ㄱㄱㅊ
# Title : Handshaking Event
# Date : 20-04-20

def edge(point):
    return (point * (point - 1)) // 2

def solution(n):
    # edge의 개수로부터 적정 인원수 people 산출
    mingyu = 0
    people = 1
    while True:
        people += 1
        if n < edge(people):
            mingyu = n - edge(people - 1)
            break
        
    return [mingyu, people]

n = int(input())
print(solution(n))

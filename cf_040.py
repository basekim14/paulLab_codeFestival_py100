# Code Festival - Python Practice 040
# Author : ㄱㄱㅊ
# Title : Going Amusement Park
# Date : 20-02-15

w_limit = int(input())
n = int(input())
weights = []

for i in range(n):
    weights.append(int(input()))

avail_n = 0

for i in range(len(weights)):
    w_limit -= weights[i]
    
    if w_limit < 0:
        print(i)
        break



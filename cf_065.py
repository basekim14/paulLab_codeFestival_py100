# Code Festival - Python Practice 065
# Author : ㄱㄱㅊ
# Title : List Apply
# Date : 20-04-19

# 두 리스트의 길이는 같다고 가정

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

c = []
count = 1

for i, j in zip(a, b):
    if count % 2 == 0:
        c.append([j, i])
    else:
        c.append([i, j])

print(c)

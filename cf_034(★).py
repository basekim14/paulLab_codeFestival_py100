# Code Festival - Python Practice 034
# Author : ㄱㄱㅊ
# Title : Implementating sort
# Date : 20-02-14

heights = list(map(int, input().split()))

if heights == sorted(heights):
    print('YES')
else:
    print('NO')

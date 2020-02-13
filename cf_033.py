# Code Festival - Python Practice 033
# Author : ㄱㄱㅊ
# Title : Printing Backward
# Date : 20-02-14

l = list(map(int, input().split()))
l.reverse()

for i in range(len(l)):
    print(l[i], end=' ')

'''
# 리스트를 뒤집지 않고 출력 순서를 역으로 하
for i in range(len1, -1, -1):
	print(l[i], end=' ')
'''

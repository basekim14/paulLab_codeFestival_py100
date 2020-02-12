# Code Festival - Python Practice 027
# Author : ㄱㄱㅊ
# Title : Making Dictionary
# Date : 20-02-12

names = input().split()
scores = list(map(int, input().split()))
# map 객체에 대하여..

myDict = dict(zip(names, scores))
print(myDict)

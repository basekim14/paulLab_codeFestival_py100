# Code Festival - Python Practice 018
# Author : ㄱㄱㅊ
# Title : Average score
# Date : 20-01-16

# kor, mat, eng = map(int, input().split())

score = dict(zip(['kor', 'mat', 'eng'], map(int, input().split())))
average = sum(score.values()) // len(score)
print(average)


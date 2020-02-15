# Code Festival - Python Practice 038
# Author : ㄱㄱㅊ
# Title : Part Time Job
# Date : 20-02-15

scores = list(map(int, input().split()))
ranks = list(set(scores))

print(scores.count(ranks[0]) + scores.count(ranks[1]) + scores.count(ranks[2]))

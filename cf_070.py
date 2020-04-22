# Code Festival - Python Practice 070
# Author : ㄱㄱㅊ
# Title : Goldbach's Conjecture
# Date : 20-04-21

import numpy as np

# 리스트 a, b는 jagged list가 아니라고 가정
def matrix_multiplication(a, b):
  if len(a[0]) != len(b):
    return -1

  return (np.matrix(a) * np.matrix(b)).tolist()

  '''

  result = [[0] * len(b[0])] * len(a)

  for i in range(len(a)):
    for j in range(len(b[0])):
      result[i][j] = a[i][j] * 

  return result
  '''


a = ([1, 2],
     [2, 4])
b = ([1, 0],
     [0, 3])

result = matrix_multiplication(a, b)
for i in range(len(result)):
    print(result[i])

# Code Festival - Python Practice 069
# Author : ㄱㄱㅊ
# Title : Goldbach's Conjecture
# Date : 20-04-21

# 함수 주석
def is_prime(a: int) -> bool:
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

def goldbach_conject(n):
    if not n > 2 or not n % 2 == 0:
        return
    
    result = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result.append((i, n - i))

    return result
    
n = int(input())
print(goldbach_conject(n))


# Code Festival - Python Practice 075
# Author : ㄱㄱㅊ
# Title : Strange 369 Game
# Date : 20-04-24
'''
def count_clap(n: int) -> int:
    num_list = [num for num in list(map(int, list(str(n // 3))))]
    return sum([num_list[::-1][i] * (3 ** i) for i in range(len(num_list))])

def count_369(n: int) -> int:
    num_list = 


    return result
'''

def is_three_mul(n):
    digit_list = list(map(int, list(str(n))))
    for digit in digit_list:
        if digit == 0 or digit % 3 != 0:
            return False
    return True

def count_369(n):
    count = 0
    for i in range(n + 1):
        if is_three_mul(i):
            count += 1        
    return count

n = int(input())
print(count_369(n))


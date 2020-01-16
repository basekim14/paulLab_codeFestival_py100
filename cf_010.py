# Code Festival - Python Practice 010
# Author : ㄱㄱㅊ
# Title : star(*) exercise
# Date : 20-01-16

num = int(input())

for i in range(num):
    space = num - (i + 1)
    star = 2 * i + 1
    print(' ' * space + '*' * star)

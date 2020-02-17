# Code Festival - Python Practice 044
# Author : ㄱㄱㅊ
# Title : The Sum of Digits
# Date : 20-02-17


# num = int(input())
# digits = list(str(num))
digits = list(map(int, input())) # 신기하네
print(sum([int(digits[i]) for i in range(len(digits))]))



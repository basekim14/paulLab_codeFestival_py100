# Code Festival - Python Practice 042
# Author : ㄱㄱㅊ
# Title : 2020
# Date : 20-02-17

days = ['WED', 'THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE']
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a, b = map(int, input().split())

total_day = sum(month[:a-1]) + b
print(days[total_day % 7 - 1])

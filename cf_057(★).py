# Code Festival - Python Practice 057
# Author : ㄱㄱㅊ
# Title : Apply Built-in Function
# Date : 20-04-16

nums_list = [str(i) for i in range(0, 1001)]
# ''.join(mylist) or str(mylist)
combined_nums = str(nums_list)
count = 0

count = combined_nums.count('1')
'''
for num in combined_nums:
    if num == '1':
        count += 1
'''

print(count)

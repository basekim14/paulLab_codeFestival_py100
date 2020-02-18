# Code Festival - Python Practice 046
# Author : ㄱㄱㅊ
# Title : 'str' Utilization
# Date : 20-02-18

nums = [i for i in range(1, 21)]
nums_str = [str(nums[i]) for i in range(20)]
full_str = ''.join(nums_str)

print(sum(list(map(int, full_str))))

# Code Festival - Python Practice 054
# Author : ㄱㄱㅊ
# Title : Continuous numbers
# Date : 20-04-14

def check_continuity(nums):
    pivot = nums[0]
    for i in range(1, len(nums)):
        pivot += 1
        if nums[i] != pivot:
            return False

    return True

nums = list(map(int, input().split()))

if check_continuity(nums):
    print('YES')
    
else:
    print('NO')

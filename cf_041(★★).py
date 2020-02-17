# Code Festival - Python Practice 041
# Author : ㄱㄱㅊ
# Title : Check Prime Number(Sieve of Eratosthenes)
# Date : 20-02-17

# my_code
checked_num = int(input())
nums = [i for i in range(2, checked_num + 1)]
start = 1

while True:
    start += 1
    if start >= checked_num:
        break

    if start not in nums:
        continue

    for i in range(nums.index(start) + 1, len(nums)):
        try:
            if nums[i] % start == 0:
                nums.remove(nums[i])
        except IndexError:
            break
        
print(nums)

# wiki_code

def prime_list(n):
    # True를 소수로 가정
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


#  1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
#  2. 2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
#  3. 자기 자신을 제외한 2의 배수를 모두 지운다.
#  4. 남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
#  5. 자기 자신을 제외한 3의 배수를 모두 지운다.
#  6. 남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
#  7. 자기 자신을 제외한 5의 배수를 모두 지운다.
#  8. 남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
#  9. 자기 자신을 제외한 7의 배수를 모두 지운다.
# 10. 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
#
# 출처 - 위키피디아, 에라토스테네스의 체

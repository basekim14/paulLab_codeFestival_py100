# Code Festival - Python Practice 058
# Author : ㄱㄱㅊ
# Title : Marking Comma
# Date : 20-04-16

num = int(input())

print(format(num, ','))
    

'''
len(str(num))
'''
'''
import mathdef digit_length(n):
    return int(math.log10(n)) + 1 if n else 0
'''
'''
def digit_length(n):
    ans = 0

    while n:
        n //= 10
        ans += 1

    return ans
'''



# https://hashcode.co.kr/questions/2959/%ED%8C%8C%EC%9D%B4%EC%8D%AC-1000%EB%8B%A8%EC%9C%84-%EC%BD%A4%EB%A7%88-%EB%84%A3%EB%8A%94%EB%B2%95
# https://shoark7.github.io/programming/algorithm/3-ways-to-get-length-of-natural-number

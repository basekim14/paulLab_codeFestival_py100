# Code Festival - Python Practice 035
# Author : ㄱㄱㅊ
# Title : Making Function 'Factory'
# Date : 20-02-14

def one(n):
    def two(val):
        num = val ** n
        
        return num
    return two

a = one(2)
b = one(3)
c = one(4)

print(a(10))
print(b(10))
print(c(10))

# 형태가 몬가 이상

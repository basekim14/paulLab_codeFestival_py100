# Code Festival - Python Practice 061
# Author : ㄱㄱㅊ
# Title : Zip String
# Date : 20-04-17

mystr = input()
result = ''
count = 0
temp = mystr[0]

for token in mystr:
    if token == temp:
        count += 1
    else:
        result += temp + str(count)
        count = 1

    temp = token

result += temp + str(count)

print(result)

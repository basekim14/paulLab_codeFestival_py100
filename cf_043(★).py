# Code Festival - Python Practice 043
# Author : ㄱㄱㅊ
# Title : Hex To Bin
# Date : 20-02-17

'''
hex_num = int(input())
bin_num = 0
mod = 0
while True:
    if hex_num < 2 ** (mod + 1):
        break
    mod += 1

for i in range(mod, -1, -1):
    if hex_num - 2 ** i >= 0:
        hex_num -= 2 ** i
        bin_num += 10 ** i

print(bin_num)

'''
hex_num = int(input())
bin_num = []

while hex_num:
    bin_num.append(str(hex_num % 2))
    hex_num //= 2

bin_num.reverse()
print(''.join(bin_num))

# 원리에 더 가까운 풀이

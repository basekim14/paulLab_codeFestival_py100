# Code Festival - Python Practice 078
# Author : ㄱㄱㅊ
# Title : Round Table(Josephus problem)
# Date : 20-06-01

print('Please enter the number of food and the number in the next order.')
N, K = map(int, input('>> ').split())

# print(N, K)
foods = [i + 1 for i in range(N)]
mod = len(foods)

# K번의 음식의 인덱스는 K - 1
idx = K - 1
# while len(foods) > 2:
while True:
    print(foods.pop(idx))
    if len(foods):
        idx = (idx + 2) % len(foods)
    else:
        break
    

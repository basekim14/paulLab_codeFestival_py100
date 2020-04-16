# Code Festival - Python Practice 055
# Author : ㄱㄱㅊ
# Title : Tower of Hanoi
# Date : 20-04-14

def hanoi(n, start, end, other):

    if n == 1:
        disk_path.append([start, end])
        return None

    hanoi(n - 1, start, other, end)
    disk_path.append([start, end])
    hanoi(n - 1, other, end, start)

disk_path = []
num = int(input())
hanoi(num, 'A', 'B', 'C')
print(disk_path)
print(len(disk_path))


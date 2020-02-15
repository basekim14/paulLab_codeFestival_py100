# Code Festival - Python Practice 037
# Author : ㄱㄱㅊ
# Title : Using count
# Date : 20-02-15

pointed = input().split()
count_num = 0

for name in pointed:
    if count_num < pointed.count(name):
        count_num = pointed.count(name)
        pointed_name = name

print('%s(이)가 총 %d표로 반장이 되었습니다.' % (pointed_name, count_num))

# Code Festival - Python Practice 051
# Author : ㄱㄱㅊ
# Title : Implementation 'merge sort'
# Date : 20-04-13

def merge_sort(mylist):
    l = len(mylist)
    
    if l <= 1:
        return mylist

    mid = l // 2
    group_1 = merge_sort(mylist[:mid])
    group_2 = merge_sort(mylist[mid:])
    result = []

    while group_1 and group_2:
        if group_1[0] < group_2[0]:
            result.append(group_1.pop(0))
        else:
            result.append(group_2.pop(0))

    while group_1:
        result.append(group_1.pop(0))
    while group_2:
        result.append(group_2.pop(0))

    return result

    
mylist = [180, 145, 165, 45, 170, 175, 173, 171]

print(merge_sort(mylist))

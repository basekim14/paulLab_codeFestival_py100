# Code Festival - Python Practice 052
# Author : ㄱㄱㅊ
# Title : Implementation 'quick sort'
# Date : 20-04-13

def quick_sort(mylist):
    l = len(mylist)

    if l <= 1:
        return mylist

    pivot = mylist.pop(l // 2)
    group_1 = []
    group_2 = []

    for i in range(l - 1):
        if mylist[i] < pivot:
            group_1.append(mylist[i])
        else:
            group_2.append(mylist[i])

    return quick_sort(group_1) + [pivot] + quick_sort(group_2)
    
mylist = [180, 145, 165, 45, 170, 175, 173, 171]

print(quick_sort(mylist))

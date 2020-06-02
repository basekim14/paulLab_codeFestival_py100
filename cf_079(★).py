# Code Festival - Python Practice 079
# Author : ㄱㄱㅊ
# Title : Iterating List
# Date : 20-06-02

def rotate(inL, inN):
    prevL = inL.copy()
    diffL = []
    
    for i in range(inN):
        inL.insert(0, inL.pop())
    '''      
    for i in range(len(inL)):
        diff = ((inL[i] - prevL[i]) ** 2) ** 0.5
        diffL.append(int(diff))
    '''

    # *****
    for i, j in zip(inL, prevL):
        diffL.append(abs(i - j))

    idx = diffL.index(min(diffL))
    print('index : %d' % idx)
    print('value : %d, %d' % (prevL[idx], inL[idx]))
    return

l = [10, 20, 25, 27, 34, 35, 39]
n = int(input('순회 횟수는 : '))

rotate(l, n)

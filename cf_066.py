# Code Festival - Python Practice 066
# Author : ㄱㄱㅊ
# Title : Block Top
# Date : 20-04-20

def check_order(tops, order):
    result = []
    for top in tops:
        tmp = []
        for token in order:
            try:
                tmp.append(top.index(token))
            except ValueError:
                pass
        result.append(tmp)

    for i in range(len(result)):
        if result[i] == sorted(result[i]):
            result[i] = '가능'
        else:
            result[i] = '불가능'
    
    return result


'''
tops = input().split()
order = input()
'''

tops = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'EFGHZ']
order = 'ABD'
print(check_order(tops, order))

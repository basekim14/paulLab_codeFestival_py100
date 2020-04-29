# Code Festival - Python Practice 077
# Author : ㄱㄱㅊ
# Title : Long Common String
# Date : 20-04-27

def common_string(s1, s2):
    common = []
    # 길이가 짧은 문자열을 기준(l2)으로
    if len(s1) > len(s2):
        l1 = list(s1)
        l2 = list(s2)
    else:
        l1 = list(s2)
        l2 = list(s1)

    

    point = 0
    for token in l2:
        for i in range(point, len(l1)):
            if l1[i] == token:
                common.append(token)
                point = i + 1
                break

    return common, len(common)

S1 = 'THESTRINGS'
S2 = 'THISIS'
print(common_string(S1, S2))

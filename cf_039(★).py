# Code Festival - Python Practice 039
# Author : ㄱㄱㅊ
# Title : Correct Typimng Error
# Date : 20-02-15

string = input()
after = ''

for i in string:
    if i == 'q':
        after += 'e'
    else:
        after += i

print(after)

'''
string.replace('e', 'q')
'''

# Code Festival - Python Practice 048
# Author : ㄱㄱㅊ
# Title : Reversal Upper and Lower Each Other
# Date : 20-02-18

string = input()
reversal_string = ''

for ch in string:
    if 'a' <= ch <= 'z':
    # if ch.islower() or ch.isupper()
        reversal_string += ch.upper()
    else:
        reversal_string += ch.lower()

print(reversal_string)

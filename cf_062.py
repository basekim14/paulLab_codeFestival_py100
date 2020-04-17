# Code Festival - Python Practice 062
# Author : ㄱㄱㅊ
# Title : Print 20190923
# Date : 20-04-17

mystr = 'aacdddddddddfffffffffgghhh'
ref = 'abcdefgh'
mydict = {}

for token in ref:
    mydict[token] = str(mystr.count(token))
    
result = ''.join(list(mydict.values()))
print(result)

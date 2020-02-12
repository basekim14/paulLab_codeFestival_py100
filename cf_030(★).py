# Code Festival - Python Practice 030
# Author : ㄱㄱㅊ
# Title : Find Word in String
# Date : 20-02-12

string = input()
word = input()

if word in string:
    print(string.find(word))

# 찾는 문자 데이터가 없는 경우
# find는 -1을 반환, index는 오류를 출력

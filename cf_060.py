# Code Festival - Python Practice 060
# Author : ㄱㄱㅊ
# Title : enumerate
# Date : 20-04-17

students = ['강은지', '김유정', '박현서', '최성훈', '홍유진', '박지호',
           '권윤일', '김채리', '한지호', '김진이', '김민호', '강채연']


for i, name in enumerate(sorted(students)):
    print("번호: {0}, 이름: {1}".format(i + 1, name))

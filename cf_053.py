# Code Festival - Python Practice 053
# Author : ㄱㄱㅊ
# Title : Parenthesis string
# Date : 20-04-13

class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        mystr = '[ '
        for i in range(len(self.stack)):
            mystr += str(self.stack[i]) + ' '
            if i != len(self.stack) - 1:
                mystr += '┃ '
            
        mystr += ']'
        
        return mystr

    def insert(self, n):
        self.stack.append(n)

    def pop(self):
        try:   
            return self.stack.pop()
        except IndexError:
            return None

def check_parenthesis(mystr):
    mylist = []
    for token in mystr:
        if token in '({[]})':
            mylist.append(token)

    S = Stack()
    for parenthesis in mylist:
        if parenthesis in '({[':
            S.insert(parenthesis)
        elif parenthesis == ')':
            if S.pop() != '(':
                return 'NO'
        elif parenthesis == '}':
            if S.pop() != '{':
                return 'NO'
        elif parenthesis == ']':
            if S.pop() != '[':
                return 'NO'

    if len(S):
        return 'NO'
        
    return 'YES'

mystr = input()
print(check_parenthesis(mystr))

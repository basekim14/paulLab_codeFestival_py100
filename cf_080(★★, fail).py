#-*- coding:utf-8 -*-
# Code Festival - Python Practice 080
# Author : ㄱㄱㅊ
# Title : Combination
# Date : 20-06-04

def factorial(n):
    # Ternary operators
    return n * factorial(n-1) if n > 1 else 1

def nPr(elems, r):
    n = len(elems)
    if 0 < n <= r:
        raise ValueError
    
    max_num = factorial(n) // factorial(n - r)
    permutations = []


            
        
        
    return permutations, max_num

def nCr(elems, r):
    n = len(elems)
    if 0 < n <= r:
        raise ValueError
    # max_num = 
    combinations = []
    # while True:
        
    return

cons = input().split(',')
com_len = int(input())

print(nPr(cons, com_len))
# print(cons)

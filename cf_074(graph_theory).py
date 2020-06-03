# Code Festival - Python Practice 074
# Author : ㄱㄱㅊ
# Title : Longest Path Search
# Date : 20-04-22

'''
def longest_path(graph, start, end):
  length_dict = dict(zip(graph.keys(), [dict(zip(graph.keys(), [0] * len(graph)))] * len(graph)))
  visited = [start]
  
      
    
  
  return length_dict[start][end]

graph = {'A': set(['B', 'C', 'D']),
         'B': set(['A', 'C', 'D', 'E', 'F']),
         'C': set(['A', 'B', 'G']),
         'D': set(['A', 'B', 'E', 'F']),
         'E': set(['B', 'D', 'F', 'G']),
         'F': set(['B', 'D', 'E', 'G']),
         'G': set(['C', 'E' 'F'])
         }

start, end = input().split()
print(longest_path(graph, start, end))
'''

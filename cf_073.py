# Code Festival - Python Practice 073
# Author : ㄱㄱㅊ
# Title : Shortest Path Search
# Date : 20-04-22

def shortest_path(graph, start, end):
  length_dict = dict(zip(graph.keys(), [dict(zip(graph.keys(), [0] * len(graph)))] * len(graph)))
  for a in graph:
    for b in graph:
      if a in graph[b]:
        length_dict[a][b] += 1
    
  
  return length_dict[start][end]

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
         }

start, end = input().split()
print(shortest_path(graph, start, end))

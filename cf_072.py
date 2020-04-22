# Code Festival - Python Practice 072
# Author : ㄱㄱㅊ
# Title : Breath-First Search
# Date : 20-04-22

graph = {
        'E': set(['D', 'A']),
        'F': set(['D']),
        'A': set(['E', 'C', 'B']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F'])
        }

def bfs(graph, start):
  visited = []
  queue = [start]

  while queue:
    n = queue.pop(0)
    
    if n not in visited:
      visited.append(n)
      queue += graph[n] - set(visited)
      
  return visited

print(bfs(graph, 'E'))

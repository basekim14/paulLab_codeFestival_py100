# Code Festival - Python Practice 071
# Author : ㄱㄱㅊ
# Title : Depth-First Search
# Date : 20-04-22

graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
        }

def dfs(graph, start):
  # 지나온 길, 돌아갈 길을 의미
  visited = []
  stack = [start]

  while stack:
    n = stack.pop()
    if n not in visited:
      visited.append(n)
      # list += set -> list = list + list(set) ...
      stack += graph[n] - set(visited)
      

  return visited

print(dfs(graph, 'E'))

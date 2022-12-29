import sys
sys.stdin = open('20924.txt')
sys.setrecursionlimit(10**8)


def gidung(start):
  global result_gidung, next_root, total_depth
  visited[start] = 1
  if (total_depth == 0 and len(graph[start]) > 1):
    return
  if len(graph[start]) <= 2:
    for node in graph[start]:
      if visited[node[0]] == 0:
        visited[node[0]] = 1
        next_root = node[0]
        result_gidung += node[1]
        total_depth += 1
        gidung(node[0])
  else:
    return

def gazi(start):
  global tmp_gazi, result_gazi
  
  for node, length in graph[start]:
    if visited[node] == 0:
      visited[node] = 1
      tmp_gazi += length
      result_gazi = max(result_gazi, tmp_gazi)
      gazi(node)
      tmp_gazi -= length

N, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
  a, b, d = map(int, input().split())
  graph[a].append((b, d))
  graph[b].append((a, d))

result_gidung, tmp_gazi, result_gazi = 0, 0, 0
total_depth = 0
next_root = R
gidung(R)
gazi(next_root)
print(result_gidung, result_gazi)
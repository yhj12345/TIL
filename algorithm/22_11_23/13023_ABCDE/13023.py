import sys
sys.stdin = open('13023.txt')


def dfs(v, cnt):
  global max_cnt
  visited[v] = 1
  if cnt+1 >= 5:
    max_cnt = max(cnt+1, max_cnt)
    return
  for node in graph[v]:
    if not visited[node]:
      dfs(node, cnt+1)
      visited[node] =0

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

max_cnt = 0
for i in range(N):
  visited = [0 for _ in range(N)]
  if max_cnt >= 5:
    break
  dfs(i, 0)

if max_cnt >= 5:
  print(1)
else:
  print(0)


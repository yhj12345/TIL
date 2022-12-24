import sys
from collections import deque
sys.stdin = open('15558.txt')

N, K = map(int, input().split())
arr1 = list(input())
arr2 = list(input())
visited = [[0 for _ in range(N)] for _ in range(2)]
answer = 0

def bfs():
  global answer
  q = deque()
  q.append((0, 0, 0))
  visited[0][0] = 1

  while q:
    flag, idx, time = q.popleft()
    if idx+1 > N-1 or idx+K > N-1:
      answer = 1
      break
    if flag == 0:
      if arr1[idx+1] == '1' and not visited[0][idx+1]:
        q.append((0, idx+1, time+1))
        visited[0][idx+1] = 1
      if arr1[idx-1] == '1' and time < idx-1 and not visited[0][idx-1]:
        q.append((0, idx-1, time+1))
        visited[0][idx-1] = 1
      if arr2[idx+K] == '1' and not visited[1][idx+K]:
        q.append((1, idx+K, time+1))
        visited[1][idx+K] = 1
    else:
      if arr2[idx+1] == '1' and not visited[1][idx+1]:
        q.append((1, idx+1, time+1))
        visited[1][idx+1] = 1
      if arr2[idx-1] == '1' and time < idx-1 and not visited[1][idx-1]:
        q.append((1, idx-1, time+1))
        visited[1][idx-1] = 1
      if arr1[idx+K] == '1' and not visited[0][idx+K]:
        q.append((0, idx+K, time+1))
        visited[0][idx+K] = 1
  
bfs()
print(answer)


import sys
from collections import deque
sys.stdin = open('3055.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    q = deque()
    visited[si][sj][0] = 1
    for wat in water:
        visited[wat[0]][wat[1]][1] = 1
        q.append((wat[0], wat[1], 1))
    q.append((si, sj, 0))

    while q:
        ti, tj, isWater = q.popleft()
        if isWater == 1:
            for k in range(4):
                ni = ti + di[k]
                nj = tj + dj[k]

                if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != 'X' and arr[ni][nj] != 'D' and visited[ni][nj][1] == 0:
                    q.append((ni, nj, 1))
                    visited[ni][nj][1] = 1
        else:
            for k in range(4):
              ni = ti + di[k]
              nj = tj + dj[k]

              if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != 'X' and arr[ni][nj] != '*' and visited[ni][nj][0] == 0 and visited[ni][nj][1] == 0:
                  q.append((ni, nj, 0))
                  visited[ni][nj][0] = visited[ti][tj][0] + 1


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

si, sj = 0, 0
ei, ej = 0, 0
water = []
visited = [[[0, 0] for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            si = i
            sj = j
        elif arr[i][j] == '*':
            water.append((i, j))
        elif arr[i][j] == 'D':
            ei, ej = i, j
bfs(si,sj)
if visited[ei][ej][0] == 0:
    print('KAKTUS')
else:
  print(visited[ei][ej][0]-1)
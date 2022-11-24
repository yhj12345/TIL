import sys
from collections import deque
sys.stdin = open('5427.txt')


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(si, sj, fire):
    q = deque()
    for f in fire:
        q.append((f[0],f[1], 1))
        visited[f[0]][f[1]][0] = -1
    visited[si][sj][1] = 1
    q.append((si, sj, 0))

    while q:
        ti, tj, what = q.popleft()
        if what == 1:
            for k in range(4):
                ni = ti + di[k]
                nj = tj + dj[k]

                if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] != '#' and -1 not in visited[ni][nj]:
                    q.append((ni, nj, 1))
                    visited[ni][nj][0] = -1
        else:
            for k in range(4):
                ni = ti + di[k]
                nj = tj + dj[k]

                if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == '.' and visited[ni][nj][0] == 0 and visited[ni][nj][1] == 0 :
                    q.append((ni, nj, 0))
                    visited[ni][nj][1] = visited[ti][tj][1] + 1
                elif 0 > ni or ni >= h or 0 > nj or nj >= w:
                    return visited[ti][tj][1]

T = int(input())

for tc in range(1, T+1):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]

    si, sj = 0, 0
    fire = []
    visited = [[[0, 0] for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                si, sj = i, j
            elif arr[i][j] == '*':
                fire.append((i, j))
    
    a = bfs(si, sj, fire)
    
    if a:
        print(a)
    else:
        print("IMPOSSIBLE")
        
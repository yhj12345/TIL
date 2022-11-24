import sys
from collections import deque
sys.stdin = open('16234.txt')


def bfs(si, sj, flag):
    global tmp
    q = deque()
    q.append((si,sj))
    visited[si][sj] = flag

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni = ti + di[k]
            nj = tj + dj[k]

            if 0 <= ni < N and 0 <= nj < N and L <= abs(arr[ti][tj] - arr[ni][nj]) <= R and not visited[ni][nj]:
                q.append((ni, nj)) 
                visited[ni][nj] = flag
                tmp += 1

N,L,R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tmp = 1
day = 0
while tmp:
    tmp = 0
    flag = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flag += 1
                bfs(i, j, flag)

    if tmp == 0:
        break
    
    open_dict = dict()
    for i in range(N):
        for j in range(N):
            if visited[i][j] in open_dict:
                open_dict[visited[i][j]][0] += arr[i][j]
                open_dict[visited[i][j]][1].append((i, j))
            else:
                open_dict[visited[i][j]]= [arr[i][j],[(i,j)]]
    # print(open_dict)
    for i in open_dict:
        a = len(open_dict[i][1])
        for x, y in open_dict[i][1]:
            arr[x][y] = open_dict[i][0] // a

    day +=1         
    print(arr)
print(day)



import sys
sys.stdin = open('1520.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(x, y):
    if x == M-1 and y == N-1: 
        return 1
    if dp[x][y] != -1: 
        return dp[x][y]
    count = 0
    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]
        if 0 <= nx < M and 0 <= ny < N and arr[x][y] > arr[nx][ny]:
            count += dfs(nx,ny)
    dp[x][y] = count
    return dp[x][y]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]



print(dfs(0, 0))
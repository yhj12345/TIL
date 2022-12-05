import sys
sys.stdin = open('1915.txt')

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]
result = 0

for i in range(n):
  if arr[i][0] == '1':
    dp[i][0] = 1
    result = 1


for j in range(m):
  if arr[0][j] == '1':
    dp[0][j] = 1
    result = 1

for i in range(1, n):
  for j in range(1, m):
    if arr[i][j] == '1':
      if dp[i-1][j] != 0 and dp[i][j-1] != 0 and dp[i-1][j-1] != 0:
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        result = max(dp[i][j], result)
      else:
        dp[i][j] = 1
        result = max(dp[i][j], result)
print(result ** 2)


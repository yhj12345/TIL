import sys
sys.stdin = open('2293.txt')

n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in coin:
  for i in range(1, k+1):
    if i-c >= 0:
      dp[i] += dp[i-c]
print(dp[k])
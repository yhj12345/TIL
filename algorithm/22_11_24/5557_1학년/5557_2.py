import sys
sys.stdin = open('5557.txt')

N = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(N-1)]
dp[0][arr[0]] += 1

for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            if j - arr[i] >= 0:
                dp[i][j-arr[i]] += dp[i-1][j]
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i-1][j]
print(dp[N-2][arr[-1]])
import sys
sys.stdin = open('2011.txt')

code = list(map(int, input()))
N = len(code)
dp = [0 for _ in range(N+1)]
if (code[0] == 0) :
    print(0)
else :
    code = [0] + code
    dp[0] = dp[1] = 1
    for i in range(2, N+1):
        if code[i] > 0:
            dp[i] += dp[i-1]
        temp = code[i-1] * 10 + code[i]
        if temp >= 10 and temp <= 26 :
            dp[i] += dp[i-2]
    print(dp[N] % 1000000)
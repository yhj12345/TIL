import sys
sys.stdin = open('19566.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = arr[0]

dict_sum = {arr[0] - K : 1}
answer = 0
if 0 in dict_sum:
  dict_sum[0] += 1
else:
  dict_sum[0] = 1
for i in range(1, N):
  dp[i] = dp[i-1] + arr[i]
  a = dp[i] - K * (i+1)

  if a not in dict_sum:
    dict_sum[a] = 0
    
  answer += dict_sum[a]
  dict_sum[a] += 1

# if 0 in dict_sum:
#   answer += dict_sum[0]
print(answer)

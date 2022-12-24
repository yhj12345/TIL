import sys
sys.stdin = open('2159.txt')

N = int(input())

# 시작 빵집
start_x, start_y = map(int, input().split())
# 배달해야할 집 리스트
delivery_list = [list(map(int, input().split())) for _ in range(N)]
# dp 배열
dp = [[0 for _ in range(5)] for _ in range(N)]

di = [0, 1, 0, -1, 0]
dj = [1, 0, -1, 0, 0]
# 빵집에서 첫 번째 집까지 거리 설정
for k in range(5):
  nx = delivery_list[0][0] + di[k]
  ny = delivery_list[0][1] + dj[k]
  dp[0][k] = abs(start_x - nx) + abs(start_y - ny)

for k in range(1, N):
  prev_x, prev_y = delivery_list[k-1][0], delivery_list[k-1][1]
  next_x, next_y = delivery_list[k][0], delivery_list[k][1]

  for i in range(5):
    nx = next_x + di[i]
    ny = next_y + dj[i]

    tmp = []
    for j in range(5):
      nnx = prev_x + di[j]
      nny = prev_y + dj[j]
      tmp.append(abs(nnx-nx) + abs(nny-ny) + dp[k-1][j])
    dp[k][i] = min(tmp)
print(min(dp[N-1]))
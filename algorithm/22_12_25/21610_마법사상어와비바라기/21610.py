import sys
sys.stdin = open('21610.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
cross_i = [-1, -1, 1, 1]
cross_j = [-1, 1, 1, -1]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for i in range(M):
  d, s = map(int, input().split())
  visited = set()

  while cloud:
    cloud_x, cloud_y = cloud.pop(-1)
    cloud_x = (cloud_x + s * di[d-1]) % N
    cloud_y = (cloud_y + s * dj[d-1]) % N
    arr[cloud_x][cloud_y] += 1
    visited.add((cloud_x, cloud_y))
  
  for cloud_x, cloud_y in visited:
    for j in range(4):
      cross_cloud_x = cloud_x + cross_i[j]
      cross_cloud_y = cloud_y + cross_j[j]
      if 0 <= cross_cloud_x < N and 0 <= cross_cloud_y < N and arr[cross_cloud_x][cross_cloud_y] > 0:
        arr[cloud_x][cloud_y] += 1
    
  for k in range(N):
    for l in range(N):
      if arr[k][l] >= 2 and (k, l) not in visited:
        cloud.append((k, l))
        arr[k][l] -= 2
  visited = set()

result = 0
for i in range(N):
  for j in range(N):
    result += arr[i][j]

print(result)
import sys
sys.stdin = open('5557.txt')

def dfs(sum, depth):
    global cnt
    if depth == N-1:
      if sum == arr[-1]:
        cnt += 1
        return
      else:
        return
    if sum+arr[depth] <= 20:
      dfs(sum+arr[depth], depth+1)
    if sum-arr[depth] >= 0:
      dfs(sum-arr[depth], depth+1)

N = int(input())
arr = list(map(int, input().split()))
cnt = 0
dfs(arr[0], 1)
print(cnt)
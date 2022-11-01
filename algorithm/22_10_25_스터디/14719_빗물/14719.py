import sys
sys.stdin = open('14719.txt')

H, W = map(int, input().split())
arr = list(map(int, input().split()))

index, result, tmp = 0, 0, 0
for i in range(1, W):
  if arr[index] <= arr[i]:
    index = i
    result += tmp
    tmp = 0
  else:
    tmp += arr[index] - arr[i]

index, tmp = W-1, 0
for i in range(W-2, -1, -1):
  if arr[index] < arr[i]:
    index = i
    result += tmp
    tmp = 0
  else:
    tmp += arr[index] - arr[i]

print(result)
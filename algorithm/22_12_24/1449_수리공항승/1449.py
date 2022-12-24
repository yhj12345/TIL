import sys
sys.stdin = open('1449.txt')

N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

answer = 1
tape = arr[0] - 0.5
for i in range(1, N):
  if tape < arr[i] < tape + L:
    continue
  else:
    answer += 1
    tape = arr[i] - 0.5
print(answer)
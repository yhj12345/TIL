import sys
sys.stdin = open('2012.txt')

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

answer = 0
for i in range(N):
  answer += abs(arr[i]-(i+1))
print(answer)
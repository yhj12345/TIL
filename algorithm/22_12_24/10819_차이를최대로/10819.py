import sys
from itertools import permutations

sys.stdin = open('10819.txt')

def cal(array):
  result = 0
  for i in range(1, N):
    result += abs(array[i-1] - array[i])
  return result

N = int(input())
arr = map(int, input().split())

answer = 0
for perm in permutations(arr, N):
  answer = max(answer, cal(perm))
print(answer)
import sys
sys.stdin = open('1083.txt')

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

max_num = 0
max_idx = 0
sort_num = 0

tmp = []
while S > 0:
  for i in range(sort_num, N):
    if max_num < arr[i] and arr[i] not in tmp:
      max_num = arr[i]
      max_idx = i
  
  if max_idx - sort_num <= S:
    arr.pop(max_idx)
    arr.insert(sort_num, max_num)
    S -= max_idx - sort_num
    sort_num += 1
    if sort_num >= N:
      break
    max_num = 0
    tmp = []
  else:
    tmp.append(max_num)
    max_num = 0

for i in arr:
  print(i, end=' ')

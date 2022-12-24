import sys
sys.stdin = open('26075.txt')

N, M = map(int, input().split())
S = list(input())
T = list(input())

S_one_idx_list = []
T_one_idx_list = []

for i in range(N+M):
  if S[i] == '1':
    S_one_idx_list.append(i)
  if T[i] == '1':
    T_one_idx_list.append(i)

result = 0
for i in range(M):
  result += abs(S_one_idx_list[i] - T_one_idx_list[i])

X = result // 2
Y = result - X

print(X ** 2 + Y ** 2)

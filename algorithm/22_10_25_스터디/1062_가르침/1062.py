import sys
sys.stdin = open('1062.txt')

def dfs(new_set, cnt, depth):
  global K, result
  if len(new_set) > K:
    return
  if depth == N:
    if len(new_set) > K:
      return
    else:
      result = max(result, cnt)
      return
  
  
  dfs(new_set, cnt, depth+1)
  dfs(new_set | set(arr[depth]), cnt+1, depth+1)
  

N, K = map(int, input().split())
arr = list(input() for _ in range(N))

attential_set = {'a', 'n', 't', 'i', 'c'}
result = 0
dfs(attential_set, 0, 0)
print(result)
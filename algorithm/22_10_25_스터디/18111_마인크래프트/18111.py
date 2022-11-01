import sys
sys.stdin = open('18111.txt')

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
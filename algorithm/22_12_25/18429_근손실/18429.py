import sys
from itertools import permutations
sys.stdin = open('18429.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for permu in permutations(arr):
    weight = 500
    for i in permu:
        weight += (i-K)
        if weight < 500:
            break
    else:
        result += 1

print(result)
import sys
sys.stdin = open('1976.txt')


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
        

N = int(input())
M = int(input())
parent = [i for i in range(N)]


for i in range(N):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j] == 1:
            union(i, j)

parent = [-1] + parent
path = list(map(int, input().split()))
start = parent[path[0]]
for i in range(1, M):
    if parent[path[i]] != start:
        print("NO")
        break
else:
    print("YES")
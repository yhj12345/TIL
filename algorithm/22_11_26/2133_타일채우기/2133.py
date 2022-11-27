import sys
sys.stdin=open('2133.txt')


N = int(input())

arr = [0 for _ in range(31)]
arr[2] = 3
arr[4] = 11

if N % 2 == 1:
    print(0)
elif N == 2:
    print(3)
else:
    for i in range(4, N+1):
        if i % 2 == 0:
            arr[i] = arr[i-2]*3 + sum(arr[:i-2])*2 + 2
    print(arr[N])

import sys
sys.stdin = open('5052.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(input() for _ in range(n))
    arr.sort()
    
    result = 'YES'
        
    for i in range(1, n):
        if arr[i].startswith(arr[i-1]):
            result = 'NO'
            break
    
    print(result)
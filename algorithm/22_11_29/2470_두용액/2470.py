import sys
sys.stdin = open('2470.txt')

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

start, end = 0, N-1
left, right = 0, N-1
tmp = 2000000001

while start < end:
    if abs(arr[start] + arr[end]) < tmp:
        left = start
        right = end

        tmp = abs(arr[start] + arr[end])

    if arr[start] + arr[end] < 0:
        start += 1
    elif arr[start] + arr[end] > 0:
        end -= 1
    else:
        break
print(arr[left], arr[right])
            

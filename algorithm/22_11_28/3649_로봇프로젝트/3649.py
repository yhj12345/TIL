import sys
sys.stdin = open('3649.txt')

while True:
    try:
        x = int(input())
        n = int(input())
        arr = list(int(input()) for _ in range(n))

        arr.sort()
        start, end = 0, n-1
        answer = 'danger'
        while start < end:
            if arr[start] + arr[end] < x * 10000000:
                start += 1
            elif arr[start] + arr[end] == x * 10000000:
                answer = 'yes'
                break
            else:
                end -= 1

        if answer == 'danger':
            print(answer)
        else:
            print(f'yes {arr[start]} {arr[end]}')
    except:
        break
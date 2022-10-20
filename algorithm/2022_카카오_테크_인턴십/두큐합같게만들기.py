from collections import deque
def solution(queue1, queue2):
    answer = -2
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    total = sum_queue1 + sum_queue2
    
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    
    result = 0
    while sum_queue1 != sum_queue2:
        if total % 2 != 0:
            break
        
        if sum_queue1 > sum_queue2:
            a = deque1.popleft()
            deque2.append(a)
            sum_queue1 -= a
            sum_queue2 += a
            result += 1
        elif sum_queue1 < sum_queue2:
            a = deque2.popleft()
            deque1.append(a)
            sum_queue1 += a
            sum_queue2 -= a
            result += 1
            
    print(result)
    
    return answer

solution([3, 2, 7, 2],[4, 6, 5, 1])
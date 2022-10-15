def solution(numbers, hand):
    answer = ''
    left_number = [1, 4, 7]
    right_number = [3, 6, 9]
    left_hand = (3, 0)
    right_hand = (3, 2)
    
    for num in numbers:
        # 숫자의 좌표를 구함
        if num != 0:
            a, b = divmod(num - 1, 3)
        else:
            a, b = 3, 1
        
        if num in right_number:
            answer += 'R'
            right_hand = (a, b)
        elif num in left_number:
            answer += 'L'
            left_hand = (a, b)
        else:
            right_distance = abs(right_hand[0] - a) + abs(right_hand[1] - b)
            left_distance = abs(left_hand[0] - a) + abs(left_hand[1] - b)
            
            if right_distance > left_distance:
                answer += 'L'
                left_hand = (a, b)
            elif right_distance < left_distance:
                answer += 'R'
                right_hand = (a, b)
            else:
                if hand == 'right':
                    answer += "R"
                    right_hand = (a, b)  
                else:
                    answer += 'L'
                    left_hand = (a, b)
    return answer
def check(array):
    human_list = []
    for i in range(5):
        for j in range(5):
            if array[i][j] == 'P':
                human_list.append((i, j))
                
    
    
    for human1 in human_list:
        for human2 in human_list:
            dist = abs(human1[0] - human2[0]) + abs(human1[1] - human2[1])
            if dist > 2 or dist == 0:
                continue
            
            elif dist == 2:
                if human1[0] == human2[0]:
                    if array[human1[0]][(human1[1] + human2[1]) // 2] != 'X':
                        return 0
                elif human1[1] == human2[1]:
                    if array[(human1[0]+human2[0])// 2][human1[1]] != 'X':
                        return 0
                else:
                    if array[human1[0]][human2[1]] != 'X' or array[human2[0]][human1[1]] != 'X':
                        return 0
            else:
                return 0
    return 1
    
def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    
    return answer
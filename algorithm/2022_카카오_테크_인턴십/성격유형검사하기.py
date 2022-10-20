def solution(survey, choices):
    answer = ''
    score_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        left = survey[i][0]
        right = survey[i][1]
        
        if choices[i] - 4 < 0:
            score_dict[left] += 4 - choices[i]
        elif choices[i] - 4 > 0:
            score_dict[right] += choices[i] - 4
            
    if score_dict['R'] >= score_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if score_dict['C'] >= score_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if score_dict['J'] >= score_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if score_dict['A'] >= score_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    print(score_dict)
    return answer
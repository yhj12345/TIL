def solution(gems):
    answer = []
    gems_type_size = len(set(gems))
    s, e = 0, 0
    result = []
    gems_dict = {gems[0] : 1}
    
    while s < len(gems) and e < len(gems):
        if len(gems_dict) == gems_type_size:
            result.append([s+1, e+1, e-s])
        
        if e == len(gems) or len(gems_dict) == gems_type_size:
            gems_dict[gems[s]] -= 1
            if gems_dict[gems[s]] == 0:
                del gems_dict[gems[s]]  
            s += 1
        else:
            e += 1
            if e == len(gems):
                break
            gems_dict[gems[e]] = gems_dict.get(gems[e], 0) + 1
    result = sorted(result, key=lambda x: (x[2]))
    answer = (result[0][0:2])
    return answer
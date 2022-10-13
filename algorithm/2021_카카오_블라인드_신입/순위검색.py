from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}
    
    for i in range(len(info)):
        new_info = info[i].split()
        info_key = new_info[:-1]   
        info_value = new_info[-1]
        
        for j in range(5):
            for combi in combinations(info_key, j):
                tmp = "".join(combi)
                if tmp in info_dict:
                    info_dict[tmp].append(int(info_value))
                else:
                    info_dict[tmp] = [int(info_value)]
    
    for k in info_dict:
        info_dict[k].sort()
        
    for i in query:
        new_query = i.split()
        query_key = new_query[:-1]
        query_value = new_query[-1]
        while 'and' in query_key:
            query_key.remove('and')
        while '-' in query_key:
            query_key.remove('-')
        query_key = "".join(query_key)
        
        if query_key in info_dict:
            scores = info_dict[query_key]
            
            if scores:
                enter = bisect_left(scores, int(query_value))
                
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
    return answer
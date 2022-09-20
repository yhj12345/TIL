def check(length, word):
    tmp = word[0:length]
    flag = 1
    cnt = length + len(word) % length
    for i in range(1, len(word) // length):
        if flag == 1 and tmp == word[i*length:(i+1)*length]:
            cnt += 1
            flag += 1
            tmp = word[i*length:(i+1)*length]
        elif flag > 1 and tmp == word[i*length:(i+1)*length]:
            tmp = word[i*length:(i+1)*length]
            flag += 1
            if flag == 10:
                cnt += 1
            elif flag == 100:
                cnt += 1
            elif flag == 1000:
                cnt += 1
        else:
            cnt += length
            flag = 1
            tmp = word[i*length:(i+1)*length]
    return cnt
            

def solution(s):
    answer = 0
    result = len(s)
    for i in range(1, len(s) // 2 + 2):
        result = min(result, check(i, s))
            
    answer = result
    return answer
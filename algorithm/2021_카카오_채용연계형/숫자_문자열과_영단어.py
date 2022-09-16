def solution(s):
    answer = 0
    result = s
    
    result = result.replace("zero", "0")
    result = result.replace("one", "1")
    result = result.replace("two", "2")
    result = result.replace("three", "3")
    result = result.replace("four", "4")
    result = result.replace("five", "5")
    result = result.replace("six", "6")
    result = result.replace("seven", "7")
    result = result.replace("eight", "8")
    result = result.replace("nine", "9")
    
    answer = int(result)
    return answer
from itertools import permutations
import copy

def operation(oper, num1, num2):
    if oper == '-':
        return int(num1) - int(num2)
    elif oper == '+':
        return int(num1)  + int(num2)
    else:
        return int(num1)  * int(num2)
    
def cal(purmutation, array):
    for k in purmutation:
        new_arr = []
        while array:
            a = array.pop(0)
            if a != k:
                new_arr.append(a)
            else:
                new_arr.append(operation(a, new_arr.pop(-1), array.pop(0)))
        array = new_arr
    return abs(new_arr[0])

def solution(expression):
    answer = 0
    operator = ['*', '-', '+']
    arr = []
    tmp = ''
    for i in range(len(expression)): 
        if expression[i] == '*' or expression[i] == "+" or expression[i] == "-":
            arr.append(tmp)
            arr.append(expression[i])
            tmp = ''
        else:
            tmp += expression[i]
    arr.append(tmp)
    result = []
    for permu in permutations(operator, 3):
        copy_arr = copy.deepcopy(arr)
        result.append(cal(permu, copy_arr))
    answer = max(result)
    return answer
from collections import deque

def solution(s):
    answer = ''
    stack = deque()
    dict = {
        "zero":'0',
        "one":'1',
        "two":'2',
        "three":'3',
        "four":'4',
        "five":'5',
        "six":'6',
        "seven":'7',
        "eight":'8',
        "nine":'9'
    }
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            stack.append(s[i])
            if ''.join(stack) in dict:
                answer += dict[''.join(stack)]
                stack.clear()
    
    return int(answer)
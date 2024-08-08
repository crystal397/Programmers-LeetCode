from collections import deque, Counter

def confirm(s):
    stack = []
    dic = {']':'[', '}':'{', ')':'('}

    # first confirm
    counter = Counter(s)
    if counter['('] != counter[')'] or counter['['] != counter[']'] or counter['{'] != counter['}']:
        return 0

    # second confirm
    for p in s:
        if dic.get(p) == None:
            stack.append(p)
        elif len(stack) != 0 and stack.pop() == dic[p]:
            continue
        else:
            return 0

    # last confirm
    if len(stack) != 0:
        return 0
    
    return 1
    

def solution(s):
    answer = 0
    q = deque(s)
    for i in range(len(s)):
        answer += confirm(''.join([str(item) for item in q]))
        p = q.popleft()
        q.append(p)
    return answer
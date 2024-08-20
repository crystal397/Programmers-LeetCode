def solution(ss):
    answer = 0
    
    def confirm(s):
        stack = []
        m = {')':'(',']':'[','}':'{'}
        for p in s:
            if p in m.values():
                stack.append(p)
            else:
                if len(stack) != 0 and stack.pop() == m[p]:
                    continue
                else:
                    return 0
        if len(stack) != 0:
            return 0
        return 1
    
    for i in range(len(ss)):
        s = ss[i:] + ss[:i]
        answer += confirm(s)
    
    return answer
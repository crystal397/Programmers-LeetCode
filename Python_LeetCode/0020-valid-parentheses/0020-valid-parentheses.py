class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', ']':'[', '}':'{'}
        for p in s:
            if p in dic.values():
                stack.append(p)
            else:
                if len(stack) != 0 and stack[-1] == dic[p]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True

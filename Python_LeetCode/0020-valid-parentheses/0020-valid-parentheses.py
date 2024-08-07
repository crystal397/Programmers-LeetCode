from collections import Counter

class Solution:
    def isValid(self, s: str) -> bool:
        # confirm the pair first
        counter = Counter(s)
        if counter['('] != counter[')'] or counter['['] != counter[']'] or counter['{'] != counter['}']:
            return False

        stack = []
        dict = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if dict.get(i) == None:
                stack.append(i)
            elif len(stack) != 0 and dict[i] == stack.pop():
                continue
            else:
                return False
        
        if len(stack) != 0:
            return False

        return True



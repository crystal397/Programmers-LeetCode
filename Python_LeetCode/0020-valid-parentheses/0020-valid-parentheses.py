class Solution:
    def isValid(self, s: str) -> bool:
        # confirm the pair
        counter = Counter(list(s))
        if counter['('] != counter[')'] or counter['['] != counter[']'] or counter['{'] != counter['}']:
            return False

        stack = []
        start = ['(', '[', '{']
        end =[')', ']', '}']
        dict = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in start:
                stack.append(i)
            elif i in end and dict[i] in stack and dict[i] == stack.pop():
                continue
            else:
                return False
        
        if len(stack) != 0:
            return False

        return True



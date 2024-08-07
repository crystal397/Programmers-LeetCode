class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        start = ['(', '[', '{']
        end =[')', ']', '}']
        dict = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in start:
                q.append(i)
            elif i in end and dict[i] in q and dict[i] == q.pop():
                continue
            else:
                return False
        
        if len(q) != 0:
            return False

        return True



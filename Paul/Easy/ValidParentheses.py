class Solution:
    def isValid(self, s: str) -> bool:
        # create dictionary with values with open and keys with closed
        # create stack to count open parenthesis
        # create loop and add open brackets to stack
        # if close check on stack if its the right close bracket
        p = {'(':')' , '[':']' , '{':'}'}
        stack = list()
        for l in s:
            if l in p.keys():
                stack.append(l)
                continue
            if stack and p[stack[-1]] == l:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
            

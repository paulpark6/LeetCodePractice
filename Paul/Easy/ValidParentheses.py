class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        b = {"(":")", "[":"]", "{":"}"}
        for p in s:
            if p in b.keys():
                stack.append(p)
            elif stack and p in b.values() and b[stack[-1]] == p:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True
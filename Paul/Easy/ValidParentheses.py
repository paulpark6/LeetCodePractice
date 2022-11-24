class Solution:
    def isValid(self, s: str) -> bool:
        # dictionary value to have open as keys and close as values
        pairs = {"{":"}", "(":")", "[":"]"}
        # stack to store open brackets
        stack = list()
        for p in s:
            # add to stack only if open
            if p in pairs:
                stack.append(p)
            # if its close check if the dict[stack[-1]] == closed bracket
            elif stack and p in pairs.values() and pairs[stack[-1]] == p:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True
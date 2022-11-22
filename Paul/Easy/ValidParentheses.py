class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"}":"{", "]":"[", ")":"("}
        stack = []
        
        for letter in s:
            if letter in lookup.values():
                stack.append(letter)
            elif stack and stack[-1] == lookup[letter]:
                stack.pop()
            else:
                return False
            
        return stack==[]
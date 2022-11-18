class Solution:
    def toLowerCase(self, s: str) -> str:
        new = ""
        for letter in s:
            if letter.isupper():
                letter = letter.lower()
            new += letter
        return new
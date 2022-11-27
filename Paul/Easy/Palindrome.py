class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
        pos = l-1
        for i in range(l//2):
            if s[i] != s[pos]:
                return False
            pos -= 1
        return True
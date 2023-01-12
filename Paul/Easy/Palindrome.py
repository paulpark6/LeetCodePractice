class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x) 
        n = len(s)
        for i in range(n//2): # loop to check for palindrome
            if s[i] != s[-(i+1)]:
                return False
                
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        def check(i):
            if i>=len(s):
                return True
            if s[i]!=s[-i-1]:
                return False
            return check(i+1)
        return check(0)
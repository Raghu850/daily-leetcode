class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        for i in range(len(s)):
            while j<len(t):
                if s[i]==t[j]:
                    j+=1
                    break
                j+=1
            else:
                return False
        return True
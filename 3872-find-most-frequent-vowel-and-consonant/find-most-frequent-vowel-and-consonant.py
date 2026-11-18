class Solution:
    def maxFreqSum(self, s: str) -> int:
        m=n=0
        for i in s:
            if i in "aeiou":
                k=s.count(i)
                m=max(m,k)
            else:
                j=s.count(i)
                n=max(n,j)
        return m+n
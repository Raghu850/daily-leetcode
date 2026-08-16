class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        b=0
        c=0
        l=1
        while l<=2*(n-c):
            i=0
            th=min(c,n-c-1)
            while i<th and s[c-i-1]==s[c+i+1]:
                i+=1
            if 2*i+1>l:
                b=c-i
                l=2*i+1
            i=0
            th=min(c+1,n-c-1)
            while i<th and s[c-i]==s[c+i+1]:
                i+=1
            if 2*i>l:
                b=c-i+1
                l=2*i
            c+=1    
        return s[b:b + l]
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h={}
        a=list(map(str,s.split()))
        n=len(pattern)
        if n!=len(a):
            return False
        
        for i in range(n):
            if pattern[i] in h:
                if h[pattern[i]] != a[i]:
                    return False
            else:
                if a[i] in h.values():
                    return False
                h[pattern[i]]=a[i]
        return True
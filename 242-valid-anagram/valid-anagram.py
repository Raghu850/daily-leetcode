class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        f=Counter(s)
        d=Counter(t)
        for i in f:
            if(f[i]!=d[i]):
                return False
        return True
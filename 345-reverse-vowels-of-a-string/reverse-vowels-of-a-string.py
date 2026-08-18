class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        k=list(s)
        v=set('aeiouAEIOU')
        while i<=j:
            if k[i] not in v:
                i+=1
            elif k[j] not in v:
                j-=1
            else:
                k[i],k[j]=k[j],k[i]
                i+=1
                j-=1
        return ''.join(k)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c=''
        n,m=len(word1),len(word2)
        i,j=0,0
        while i<n and j<m:
            c+=word1[i]
            c+=word2[j]
            i+=1
            j+=1
        while i<n:
            c+=word1[i]
            i+=1
        while j<m:
            c+=word2[j]
            j+=1
        return c

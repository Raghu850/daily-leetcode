class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        cnt=set()
        for i in freq.values():
            if i in cnt:
                return False
            cnt.add(i)
        return True
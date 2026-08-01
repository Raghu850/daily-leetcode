class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h={0:1}
        s=0
        res=0
        for i in nums:
            s+=i
            res+=h.get(s-k,0)
            h[s]=1+h.get(s,0)
        return res
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        m=0
        for i in nums:
            if i:
                cnt+=1
            else:
                m=max(m,cnt)
                cnt=0
        m=max(m,cnt)
        return m

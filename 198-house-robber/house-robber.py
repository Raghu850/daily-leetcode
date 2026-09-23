class Solution:
    def rob(self, nums: List[int]) -> int:
        pre,m=0,0
        for i in nums:
            temp=max(m,pre+i)
            pre,m=m,temp
        return m
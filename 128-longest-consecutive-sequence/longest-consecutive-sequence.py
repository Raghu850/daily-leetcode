class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       h=set(nums)
       m=0
       for i in h:
        if (i-1) not in h:
            count=1
            while i+count in h:
                count+=1
            m=max(m,count)
       return m
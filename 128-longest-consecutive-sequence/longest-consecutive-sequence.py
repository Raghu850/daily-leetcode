class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set(nums)
        longest=0
        cnt=0
        for i in h:
            if i-1 not in h:
                cnt=1
                while i+cnt in h:
                    cnt+=1
            longest=max(longest,cnt)
        return longest
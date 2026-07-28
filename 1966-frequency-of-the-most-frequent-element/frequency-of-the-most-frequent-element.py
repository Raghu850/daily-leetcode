class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        s=0
        ans=1
        for r in range(len(nums)):
            s+=nums[r]
            while nums[r]*(r-l+1)-s>k:
                s-=nums[l]
                l+=1
            ans=max(ans,r-l+1)
        return ans
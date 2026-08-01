class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                cnt=1
                ele=nums[i]
            elif nums[i]==ele:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in range(len(nums)):
            if nums[i]==ele:
                cnt1+=1
        if cnt1>len(nums)//2:
            return ele
        return -1
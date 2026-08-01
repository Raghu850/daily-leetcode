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
        return ele
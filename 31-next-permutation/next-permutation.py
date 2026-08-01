class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        ind=1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        else:
            nums.reverse()
            return
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
        m=(n+ind)//2
        ind+=1
        for i in range(n-1,m,-1):
            nums[i],nums[ind]=nums[ind],nums[i]
            ind+=1
        
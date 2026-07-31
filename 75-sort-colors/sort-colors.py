class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[i],nums[mid]=nums[mid],nums[i]
                i+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        
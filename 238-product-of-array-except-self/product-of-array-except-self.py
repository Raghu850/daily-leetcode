class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_li = []
        for i in nums:
            prefix_li.append(prefix)
            prefix = prefix*i
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            prefix_li[i] = prefix_li[i]*suffix
            suffix = suffix*nums[i]
        return prefix_li

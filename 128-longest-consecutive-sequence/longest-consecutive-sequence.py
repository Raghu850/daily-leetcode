class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        longest_len = 0
        start = 0
        if len(nums) < 2:
            return len(nums)
        for idx in range(1,len(nums)):
            if nums[idx] - nums[idx-1] != 1:
                longest_len = max(longest_len, idx - start)
                start = idx
        longest_len = max(longest_len, idx - start + 1)
        return longest_len
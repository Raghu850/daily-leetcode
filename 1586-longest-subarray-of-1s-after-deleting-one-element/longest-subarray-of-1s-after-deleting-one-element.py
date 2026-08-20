class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        has_zero = False
        encounter_zero = False
        prev_0 = -1
        size = 0
        tr = 0
        for i, n in enumerate(nums):
            if n:
                size += 1
            else:
                encounter_zero = True
                if has_zero:
                    size = i - prev_0 - 1
                    size = size if size>0 else 0
                has_zero = True if size else False
                prev_0 = i
            if size > tr:
                tr = size
                
        if encounter_zero:
            return tr
        else:
            return max(tr-1, 0)
                
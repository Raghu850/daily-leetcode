from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        ans = []
        t = len(nums) // 3

        for i, j in c.items():
            if j > t:
                ans.append(i)

        return ans
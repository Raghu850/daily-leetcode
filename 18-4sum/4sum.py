class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        def two_sum(nums, target):
            seen = set()
            res = set()
            for num in nums:
                if target - num in seen:
                    res.add((target - num, num))
                seen.add(num)
            
            return res

        def k_sum(nums, target, k):

            res = []

            average = target // k

            if nums[0] > average or nums[-1] < average:
                return res

            if k == 2:
                return two_sum(nums, target)
            else:
                for idx in range(len(nums) - k + 1):
                    if idx > 0 and nums[idx - 1] == nums[idx]:
                        continue 
                    results = k_sum(nums[idx + 1:], target - nums[idx], k - 1)
                    for result in results:
                        result = list(result)
                        result.append(nums[idx])
                        res.append(result)
            return res

        return k_sum(nums, target, 4)
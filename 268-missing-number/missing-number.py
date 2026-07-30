class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        for i in range(n):
            sum+=nums[i]
        sumofn=(n+1)*(n)//2
        return sumofn-sum
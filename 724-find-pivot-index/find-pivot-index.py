class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[0]*n
        pre_sum=0
        for i in range(n):
            pre[i]=pre_sum
            pre_sum+=nums[i]
        suf_sum=0
        for i in range(n-1,-1,-1):
            pre[i]=pre[i]-suf_sum
            suf_sum+=nums[i]
        for i in range(n):
            if pre[i]==0:
                return i
        return -1
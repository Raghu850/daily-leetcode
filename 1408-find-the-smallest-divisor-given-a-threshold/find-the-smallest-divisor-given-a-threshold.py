class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        if n>threshold: return -1
        l,h=1,max(nums)
        ans=-1
        def sumofd(d):
            s=0
            for i in nums:
                s+=math.ceil(i/d)
            return s
        while l<=h:
            mid=(l+h)//2
            if sumofd(mid)<=threshold:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l,h=0,len(arr)-1
        while l<=h:
            mid=(l+h)//2
            miss=arr[mid]-(mid+1)
            if miss<k:l=mid+1
            else:h=mid-1
        return h+1+k

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,h=max(weights),sum(weights)
        while l<=h:
            mid=(l+h)//2
            day,load=1,0
            for i in weights:
                if load+i>mid:
                    day=day+1
                    load=i
                else:
                    load+=i
            if day<=days:
                h=mid-1
            else:
                l=mid+1
        return l
            
            
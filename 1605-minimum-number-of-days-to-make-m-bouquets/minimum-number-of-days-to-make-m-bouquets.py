class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:return -1
        l,h=min(bloomDay),max(bloomDay)
        def possible(day):
            cnt=0
            nb=0
            for i in bloomDay:
                if i<=day:
                    cnt+=1
                else:
                    nb+=cnt//k
                    cnt=0
            nb+=cnt//k
            if nb>=m:return True
            else:return False
        ans=-1
        while l<=h:
            mid=(l+h)//2
            if possible(mid):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
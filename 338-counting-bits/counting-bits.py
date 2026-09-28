class Solution:
    def countBits(self, n: int) -> List[int]:
        sum=[0]*(n+1)
        for i in range(1,n+1):
            sum[i]=sum[i >> 1] + (i & 1)
        return sum 
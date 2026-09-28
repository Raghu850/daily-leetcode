class Solution:
    ans=[0]
    for i in range(1,10**5+1):
        ans.append(ans[i>>1]+(i&1))
    def countBits(self, n: int) -> list[int]:
        return self.ans[:n+1]
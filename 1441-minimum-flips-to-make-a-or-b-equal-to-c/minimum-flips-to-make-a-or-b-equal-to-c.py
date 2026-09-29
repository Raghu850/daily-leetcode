class Solution:
    def minFlips(self, a, b, c):
        flips = 0
        for i in range(30):
            ba, bb, bc = (a>>i)&1, (b>>i)&1, (c>>i)&1
            if bc: flips += (1 if not ba and not bb else 0)
            else: flips += ba + bb
        return flips
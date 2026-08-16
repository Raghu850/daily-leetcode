class Solution:
    def romanToInt(self, s: str) -> int:
        a={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        count = 0
        prev = 0
        
        for i in s[::-1]:  # Loop from right to left
            b = a.get(i)
            if b < prev:
                count -= b
            else:
                count += b
                prev = b
        return count
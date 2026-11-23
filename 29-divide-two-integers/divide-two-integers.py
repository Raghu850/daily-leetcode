class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = (2**31)-1
        MIN_INT = -2**31
        num = abs(dividend)
        den = abs(divisor)
        quotient = 0
        while num >= den:
            temp_den = den
            multiple = 1
            while num >= (temp_den << 1):
                temp_den = temp_den << 1
                multiple = multiple << 1
            num -= temp_den
            quotient += multiple
        is_negative = (dividend < 0) != (divisor < 0)
        ans = -quotient if is_negative else quotient
        if ans > MAX_INT:
            return MAX_INT
        elif ans < MIN_INT:
            return MIN_INT
        else:
            return ans
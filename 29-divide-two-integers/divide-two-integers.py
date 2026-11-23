class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        # The only case where 32-bit integer division overflows
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine if the final quotient should be negative
        negative = (dividend < 0) != (divisor < 0)

        a, b = abs(dividend), abs(divisor)
        quotient = 0

        while a >= b:
            temp = b
            multiple = 1
            # Double temp and multiple until the next doubling exceeds a
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            quotient += multiple

        return -quotient if negative else quotient
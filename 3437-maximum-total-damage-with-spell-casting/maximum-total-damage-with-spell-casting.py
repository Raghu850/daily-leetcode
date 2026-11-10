class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        
        # dp = [0] * (max(power)+1)
        power.sort()

        dp1, dp2, dp3 = 0, 0, 0
        prev = None
        prev_prev = None
        i = 0
        
        while i < len(power):
            p = power[i]
            curr_p = p
            while i + 1 < len(power) and power[i + 1] == p:
                curr_p += p
                i += 1

            if prev == None:
                dp1 = curr_p
            elif p - prev > 2:
                dp1, dp2, dp3 = dp1 + curr_p, dp1, dp2
            elif prev_prev and p - prev_prev > 2:
                dp1, dp2, dp3 = max(dp1, dp2+curr_p), dp1, dp2
            else:
                dp1, dp2, dp3 = max(dp1, dp3+curr_p), dp1, dp2

            prev, prev_prev = p, prev
            i += 1
        
        return max(dp1, dp2, dp3)
            


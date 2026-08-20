class Solution:
    def maxVowels(self, s: str, k: int):
        a = set('aeiou')
        cnt = 0

        for i in range(k):
            if s[i] in a:
                cnt += 1

        ans = cnt

        for i in range(k, len(s)):
            if s[i - k] in a:
                cnt -= 1

            if s[i] in a:
                cnt += 1

            ans = max(ans, cnt)

        return ans
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [0] * (COLS+1)
        res = 0
        for r in range(ROWS-1, -1, -1):
            tempDP = [0] * (COLS+1)
            for c in range(COLS-1,-1,-1):
                if matrix[r][c] == 1:
                    tempDP[c] = 1 + min(dp[c], tempDP[c+1], dp[c+1])
                    res += tempDP[c]
            dp = tempDP
        return res
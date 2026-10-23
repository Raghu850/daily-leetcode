List = list

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def reachable(starts):
            seen = [[False] * n for _ in range(m)]
            stack = []

            for r, c in starts:
                if not seen[r][c]:
                    seen[r][c] = True
                    stack.append((r, c))

            while stack:
                r, c = stack.pop()

                if r > 0 and not seen[r - 1][c] and heights[r - 1][c] >= heights[r][c]:
                    seen[r - 1][c] = True
                    stack.append((r - 1, c))
                if r + 1 < m and not seen[r + 1][c] and heights[r + 1][c] >= heights[r][c]:
                    seen[r + 1][c] = True
                    stack.append((r + 1, c))
                if c > 0 and not seen[r][c - 1] and heights[r][c - 1] >= heights[r][c]:
                    seen[r][c - 1] = True
                    stack.append((r, c - 1))
                if c + 1 < n and not seen[r][c + 1] and heights[r][c + 1] >= heights[r][c]:
                    seen[r][c + 1] = True
                    stack.append((r, c + 1))

            return seen

        pacific_starts = []
        atlantic_starts = []

        for c in range(n):
            pacific_starts.append((0, c))
            atlantic_starts.append((m - 1, c))

        for r in range(m):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, n - 1))

        pacific = reachable(pacific_starts)
        atlantic = reachable(atlantic_starts)

        result = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result
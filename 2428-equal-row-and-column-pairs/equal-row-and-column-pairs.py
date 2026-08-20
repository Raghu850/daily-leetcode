class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq={}
        for row in grid:
            r=tuple(row)
            freq[r]=freq.get(r,0)+1
        ans=0
        n=len(grid)
        for j in range(n):
            col=[]
            for i in range(n):
                col.append(grid[i][j])
            c=tuple(col)
            if c in freq:
                ans+=freq[c]
        return ans
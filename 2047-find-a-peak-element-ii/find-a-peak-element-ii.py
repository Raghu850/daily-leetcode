class Solution:
    def findPeakGrid(self, mat):
        ans = [0, 0]
        max_val = float('-inf')

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] > max_val:
                    max_val = mat[i][j]
                    ans = [i, j]

        return ans
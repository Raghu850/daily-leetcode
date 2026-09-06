class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        vis = [False] * m
        def dfs(node):
            vis[node] = True
            for j in range(m):
                if not vis[j] and isConnected[node][j] == 1 and node != j:
                    dfs(j)

        count = 0
        for i in range(m):
            if not vis[i]:
                dfs(i)
                count += 1

        return count
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root.left, True, 0), self.dfs(root.right, False, 0))

    def dfs(self, root, isLeft, length):
        if not root:
            return length
        
        if isLeft:
            return max(self.dfs(root.right, False, length+1), self.dfs(root.left, True, 0))
        else:
            return max(self.dfs(root.left, True, length+1), self.dfs(root.right, False, 0))
      
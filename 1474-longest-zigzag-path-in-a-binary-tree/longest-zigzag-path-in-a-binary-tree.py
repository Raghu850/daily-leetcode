# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, goLeft, length):
            if not node:
                return
            # update max answer so far
            self.ans = max(self.ans, length)

            if goLeft:
                # if going left now, next must be right
                dfs(node.left, False, length + 1)
                # OR restart fresh on right
                dfs(node.right, True, 1)
            else:
                dfs(node.right, True, length + 1)
                dfs(node.left, False, 1)

        dfs(root, True, 0)   # assume starting left
        dfs(root, False, 0)  # assume starting right
        return self.ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []
        def f(root, sum, path):
            if not root:
                return
            sum += root.val
            path.append(root.val)
            if not root.left and not root.right and sum == targetSum:
                ans.append(path.copy())
                path.pop()
                return
            f(root.left, sum, path)
            f(root.right, sum, path)
            path.pop()
        f(root, 0, [])
        return ans
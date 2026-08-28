# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.count = 1
        def count_good(node, maximum_on_path):
            if not node:
                return
            if node.val >= maximum_on_path:
                self.count += 1
                maximum_on_path = node.val
            count_good(node.left, maximum_on_path)
            count_good(node.right, maximum_on_path)
        count_good(root.left, root.val)
        count_good(root.right, root.val)
        return self.count    
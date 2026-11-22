# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def find(node,path,cur):
            if not node:
                return 
            cur+=node.val
            path.append(node.val)
            if not node.left and not node.right and cur==targetSum:
                res.append(path[:])

            find(node.left,path,cur)
            find(node.right,path,cur)
            path.pop()
        find(root, [],0)
        return res
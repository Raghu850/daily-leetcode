# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftvalue =  self.longestfromcur(root.left,1,1) if root.left else 0
        rightvalue = self.longestfromcur(root.right,0,1) if root.right else 0
       
        return max(leftvalue,rightvalue)



    def longestfromcur(self,cur,handiness,depth):
        '''
        longest length from the cur node, when the current node takes the handiness action. there s already depth number consecutive 
        '''
        if (not cur.left) and (not cur.right):
            return depth
        if handiness ==0:
            leftvalue =depth
            rightvalue =depth
            if cur.left:
                leftvalue = self.longestfromcur(cur.left,1,depth+1)
            if cur.right :
                rightvalue =  self.longestfromcur(cur.right,0,1)
            return max(leftvalue,rightvalue)
        else:
        
            leftvalue =depth
            rightvalue =depth
            if cur.left:
                leftvalue = self.longestfromcur(cur.left,1,1)
            if cur.right :
                rightvalue = self.longestfromcur(cur.right,0,depth+1)
            return max(leftvalue,rightvalue)
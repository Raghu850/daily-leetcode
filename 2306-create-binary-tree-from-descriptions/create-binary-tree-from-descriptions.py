# # # Definition for a binary tree node.
# # # class TreeNode:
# # #     def __init__(self, val=0, left=None, right=None):
# # #         self.val = val
# # #         self.left = left
# # #         self.right = right
# # class Solution:
# #     def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
# #         # nodes = {}
# #         # child = set()
# #         # for p, c, isleft in descriptions:
# #         #     child.add(c)

# #         #     if p not in nodes:
# #         #         nodes[p] = TreeNode(p)
# #         #     if c not in nodes:
# #         #         nodes[c] = TreeNode(c)

# #         #     if isleft:
# #         #         nodes[p].left = nodes[c]
# #         #     else:
# #         #         nodes[p].right = nodes[c]

# #         # for node in nodes:
# #         #     if node not in child:
# #         #         return nodes[node]






# #         nodes = {}
# #         root = None
# #         for _, c, _ in descriptions:
# #             if c not in nodes:
# #                 nodes[c] = TreeNode(c) 

# #         for p, c, isleft in descriptions:

# #             if p not in nodes:
# #                 nodes[p] = TreeNode(p)
# #                 root = nodes[p]

# #             if isleft:
# #                 nodes[p].left = nodes[c]
# #             else:
# #                 nodes[p].right = nodes[c]

# #         return root






# class Solution:
#     def createBinaryTree(self, A: List[List[int]]) -> Optional[TreeNode]:
#         nodes = {}
#         root = 0

#         for x, y, is_left in A:
#             if x not in nodes:
#                 nodes[x] = TreeNode(x)
#                 root ^= x
#             if y not in nodes:
#                 nodes[y] = TreeNode(y)
#                 root ^= y
#             if is_left:
#                 nodes[x].left = nodes[y]
#             else:
#                 nodes[x].right = nodes[y]
#             root ^= y

#         return nodes[root]






class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = [None] * 100001
        root = None
        
        for _, v, _ in descriptions:
            nodes[v] = TreeNode(v)
            
        for u, v, left in descriptions:
            if nodes[u] is None:
                nodes[u] = TreeNode(u)
                root = nodes[u]
                
            if left == 1:
                nodes[u].left = nodes[v]
            else:
                nodes[u].right = nodes[v]
                
        return root
        
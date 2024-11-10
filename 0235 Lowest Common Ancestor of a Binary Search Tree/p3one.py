# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommon(self, node: 'TreeNode', p: int, q: int) -> 'TreeNode':
        if not node:  
            return None

        if node.val > q and node.val > p:
            return self.lowestCommon(node.left, p, q)

        if node.val < q and node.val < p: 
            return self.lowestCommon(node.right, p, q)
        
        return node


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        return self.lowestCommon(root, p.val, q.val)

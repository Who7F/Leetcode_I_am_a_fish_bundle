# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        prev_val = None  
        anc = 10**5  

        def in_order(node):
            nonlocal prev_val, anc
            if not node:
                return

            in_order(node.left)
            
            if prev_val is not None:
                anc = min(anc, node.val - prev_val)
            
            prev_val = node.val
            
            in_order(node.right)

        in_order(root)  
        return anc

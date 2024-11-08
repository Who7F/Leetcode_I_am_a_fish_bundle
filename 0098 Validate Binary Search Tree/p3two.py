# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValid(self, node, lit, big) -> bool:
        if not node:
            return True
        
        if node.val <= lit or node.val >= big:
            return False

        return self.isValid(node.left, lit, node.val) and self.isValid(node.right, node.val, big)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))
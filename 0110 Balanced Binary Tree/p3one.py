# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkBalance(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
            
        left_depth = self.checkBalance(root.left)
        if left_depth == -1: return -1

        right_depth = self.checkBalance(root.right)
        if right_depth == -1: return -1

        if (left_depth - right_depth) > 1: return -1

        return 1 + max(left_depth, right_depth) 


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalance(root) != -1

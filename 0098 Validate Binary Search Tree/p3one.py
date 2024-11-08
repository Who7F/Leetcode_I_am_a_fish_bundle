# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val = None
        self.result = True

    def isOrder(self, node: Optional[TreeNode]):
        if not node:
            return

        if self.result == False:
            return

        self.isOrder(node.left) 
        
        if self.val is not None and self.val >= node.val:
            self.result = False

        self.val = node.val

        self.isOrder(node.right) 

        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isOrder(root)
        return self.result
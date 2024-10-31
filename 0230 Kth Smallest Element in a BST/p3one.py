# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.anc = 0
        self.k = 0

    def getKth(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        self.getKth(root.left)
        
        self.k -= 1

        if self.k == 0:
            self.anc = root.val
        elif self.k > 0:
            self.getKth(root.right)

        return
        

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.getKth(root)

        return self.anc
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diemeter = 0

    def hightOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_branch = self.hightOfBinaryTree(root.left)
        right_branch = self.hightOfBinaryTree(root.right)

        self.max_diemeter = max(self.max_diemeter, left_branch + right_branch)

        return max(left_branch, right_branch) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.hightOfBinaryTree(root)

        return self.max_diemeter

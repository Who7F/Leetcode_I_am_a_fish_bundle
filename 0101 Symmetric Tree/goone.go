/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isMirror(left *TreeNode, right *TreeNode) bool {
    if left == nil && right == nil {
        return true
    }
    if left == nil || right == nil {
        return false
    }
    return left.Val == right.Val && isMirror(left.Left, right.Right) && isMirror(left.Right, right.Left)
}

func isSymmetric(root *TreeNode) bool {
    return isMirror(root.Left, root.Right)
}
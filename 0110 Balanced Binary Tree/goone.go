/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func max(x int, y int) int {
    if x > y {
        return x
    }
    return y
}

func abs(n int) int{
    if n > 0{
        return n
    }
    return -n
}

func checkBalance(root *TreeNode) int {
    if root == nil {
        return 0
    }
    leftDepth := checkBalance(root.Left)
    if leftDepth == -1 {
        return -1
    }
    rightDepth := checkBalance(root.Right)
    if rightDepth == -1 {
        return -1
    }
    if abs(leftDepth - rightDepth) > 1 {
        return -1
    }

    return 1 + max(leftDepth, rightDepth)
}

func isBalanced(root *TreeNode) bool {
    return checkBalance(root) != -1
}
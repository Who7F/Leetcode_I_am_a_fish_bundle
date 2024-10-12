/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func max(x int, y int) int {
    if x > y{
        return x
    }
    return y
}

func maxDepth(root *TreeNode) int {
    if root == nil{
        return 0
    }else{
        return 1 + max(maxDepth(root.Left), maxDepth(root.Right))
    }
}
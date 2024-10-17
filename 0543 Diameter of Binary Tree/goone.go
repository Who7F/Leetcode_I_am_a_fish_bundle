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

func hightOfBinaryTree(root *TreeNode, maxDiemeter *int) int {
    if root == nil {
        return 0
    }
    leftHeight := hightOfBinaryTree(root.Left, maxDiemeter)
    rightHeight := hightOfBinaryTree(root.Right, maxDiemeter)

    *maxDiemeter = max(*maxDiemeter, leftHeight + rightHeight)

    return max(leftHeight, rightHeight) + 1    
}
 
func diameterOfBinaryTree(root *TreeNode) int {
    maxDiemeter := 0
    hightOfBinaryTree(root, &maxDiemeter)
    return maxDiemeter
}
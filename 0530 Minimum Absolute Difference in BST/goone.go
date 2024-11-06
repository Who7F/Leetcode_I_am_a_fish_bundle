/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func min(x int, y int) int {
    if x < y {
        return x
    }
    return y
}

func InOrder(node *TreeNode, prev **int) int {
    if node == nil{
        return 10000000
    }
 
    anc := InOrder(node.Left, prev)
    
    if *prev != nil {
        anc = min(anc, node.Val - **prev)
    }

    *prev = &node.Val;
            
    anc = min(anc, InOrder(node.Right, prev))

    return anc
}

func getMinimumDifference(root *TreeNode) int {
    var prev *int = nil
    return InOrder(root, &prev)
}
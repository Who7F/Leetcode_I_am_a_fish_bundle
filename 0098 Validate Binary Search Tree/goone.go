/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import (
    "math"
)

func isValid(node *TreeNode, lit int64, big int64) bool {
    if node == nil {
        return true
    }
    
    if int64(node.Val) <= lit || int64(node.Val) >= big {
        return false
    }

    return isValid(node.Left, lit, int64(node.Val)) && isValid(node.Right, int64(node.Val), big)
}

func isValidBST(root *TreeNode) bool {
    return isValid(root, math.MinInt64, math.MaxInt64)
}
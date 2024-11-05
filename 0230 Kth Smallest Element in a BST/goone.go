/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getkth(root *TreeNode, k *int, anc *int) {
    if root == nil {
        return
    }
    getkth(root.Left, k, anc)
    (*k)--
    if *k == 0 {
        *anc = root.Val
    } else if *k > 0 {
        getkth(root.Right, k, anc)
    }
    return
}

func kthSmallest(root *TreeNode, k int) int {
    anc := 0
    getkth(root, &k, &anc)
    return anc
}
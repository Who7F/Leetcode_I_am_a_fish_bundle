/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */

func commonAncestor(node *TreeNode, q int, p int) *TreeNode {
	if node == nil {
        return node
    }

    if node.Val > q && node.Val > p {
         return commonAncestor(node.Left, q, p)
    }

    if node.Val < q && node.Val < p {
         return commonAncestor(node.Right, q, p)
    }

    return node
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	return commonAncestor(root, q.Val, p.Val)
}

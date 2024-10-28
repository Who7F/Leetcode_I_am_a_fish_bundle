/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return [][]int{}
    }
    queue := list.New()
    queue.PushBack(root)
    anc := [][]int{}

    for queue.Len() > 0 {
        n := queue.Len()
        level := []int{}

        for i := 0; i < n; i++ {
            node := queue.Remove(queue.Front()).(*TreeNode)
            level = append(level, node.Val)

            if node.Left != nil {
                queue.PushBack(node.Left)
            }
            if node.Right != nil {
                queue.PushBack(node.Right)
            }
        }
        anc = append(anc, level)
    }
    return anc
}
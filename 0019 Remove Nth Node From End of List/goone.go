/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    bigDaddyD := &ListNode{0, head}
    blindAl := bigDaddyD
    for i := 0; i < n; i++ {
        head = head.Next
    }
    for head != nil{
        head = head.Next
        blindAl = blindAl.Next
    }
    blindAl.Next = blindAl.Next.Next

    return bigDaddyD.Next
}
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil{
        return head
    }
    h := head
    for h.Next != nil {
        if h.Val == h.Next.Val{
            h.Next = h.Next.Next
        } else {
            h = h.Next
        }
    }
    return head
}
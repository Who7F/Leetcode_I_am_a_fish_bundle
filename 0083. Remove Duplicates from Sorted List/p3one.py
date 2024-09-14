class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        h = head
        while h.next:
            if h.val == h.next.val:
                h.next = h.next.next
            else:
                h = h.next

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        tail.next = head

        curr = head
        prev = None

        k %= n

        for _ in range(n - k):
            prev = curr
            curr = curr.next

        prev.next = None
        return curr

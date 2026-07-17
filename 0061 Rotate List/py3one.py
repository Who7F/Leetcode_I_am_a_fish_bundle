# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def headToTale(self, head, node):
        if node.next == None:
            node.next = head
            return 1
            
        return 1 + self.headToTale(head, node.next)
       

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        l = self.headToTale(head, head) 
        k %= l
        old_head = head
        

        for _ in range(l - k):
            old_head = head
            head = head.next

        old_head.next = None

        return head

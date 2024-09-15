"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':   
        if not head: return head

        node_map = {}
        h = head

        while h:
            node_map[h] = Node(h.val, None, None)
            h = h.next

        h = head

        while h:
            node_map[h].random = node_map.get(h.random)
            node_map[h].next = node_map.get(h.next) 
            h = h.next  
  
        return node_map[head]

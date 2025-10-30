"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        seen = {node: Node(node.val)}
        que = deque([node])

        while que:
            curr = que.popleft()
            for n in curr.neighbors:
                if n not in seen:
                    seen[n] = Node(n.val)
                    que.append(n)
                seen[curr].neighbors.append(seen[n]) 
        
        return seen[node]

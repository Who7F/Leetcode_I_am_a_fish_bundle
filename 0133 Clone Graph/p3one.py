"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node, seen):
        if node in seen:
            return seen[node]

        clone = Node(node.val)
        seen[node] = clone
        
        for n in node.neighbors:
            clone.neighbors.append(self.dfs(n, seen))

        return clone
        

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        seen = {}
        
        return self.dfs(node, seen)
        
        

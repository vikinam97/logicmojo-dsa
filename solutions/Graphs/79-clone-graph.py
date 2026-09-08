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
            return
            
        cloneRef = {}

        def dfs(n):
            if not n:
                return
            
            cloned = None
            if n.val in cloneRef:
                cloned = cloneRef[n.val]
                return cloned

            cloned = Node(n.val)
            cloneRef[n.val] = cloned
            
            for nxt in n.neighbors:
                cloned.neighbors.append(dfs(nxt))
            
            return cloned

        dfs(node)

        return cloneRef[node.val]

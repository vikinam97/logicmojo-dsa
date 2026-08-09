# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(lambda: defaultdict(list))

        def dfs(node, r, c):
            if not node:
                return
            
            columns[c][r].append(node.val)

            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
        
        dfs(root, 0, 0)
        lmin, lmax = min(list(columns)), max(list(columns))

        result = []
        while lmin <= lmax:
            level = []

            rmin, rmax = min(list(columns[lmin])), max(list(columns[lmin]))

            while rmin <= rmax:
                row = columns[lmin][rmin]
                if len(row) > 1:
                    row.sort()
                level.extend(row[:])
                rmin += 1
                
            result.append(level)
            lmin += 1

        return result

        